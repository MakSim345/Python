Многопоточное скачивание файлов с ftp python-скриптом

Зачем это нужно?
Однажды передо мной встала задача копирования большого количества файлов с ftp-сервера. Нужно было делать бэкап. Казалось бы, что может быть проще! Но увы, ничего готового работающего так же быстро для моих условий найти не удалось.

Ситуация
Нужно было забирать периодически пару сотен файлов с ftp-сервера под Windows. Много мелочи и несколько очень крупных по размеру файлов. Суммарно примерно на 500 Гб. Сервер представляет собой vps, расположенный довольно далеко за рубежом. Днем машина высоко нагружена, рано ночью выполняются регламентные работы, итого на скачивание часов 5 максимум.

Ни одна из рассмотренных мной утилит не смогла справиться качественно и за отведенное время. Ну что ж, деваться некуда, нормальную систему резервного копирования ещё не купили, а значит ноги в руки вооружаемся редактором или IDE Python и вперёд! За приключениями!

Конфиг
Все параметры для скрипта вынесем в отдельный файл для удобства.

Шаблон конфига:

host = 'ip.ip.ip.ip'
user = 'ftpusername'
passwd = 'ftppassword'
basepath = '/path/to/backup/folder'  # Папка, в которой будут созданы подпапки со скачанными файлами
max_threads = 20 # максимальное количество одновременных процессов загрузки
log_path = '\path\to\logfile'
statusfilepath = '\path\to\statusfile'
Конфиг сохраняем с расширением .py и импортируем в начале нашего скрипта. Импортировать можно непосредственно в пространство имён скрипта, но я сделал конструкцию слегка напоминающую костыль в основной части моего скрипта:

if __name__ == "__main__":
    host = config.host
    user = config.user
    passwd = config.passwd
    basepath = config.basepath  # Папка, в которой будут созданы подпапки со скачанными файлами
    max_threads = config.max_threads
    log_path = config.log_path
    statusfilepath = config.statusfilepath
    main()
В начале был список
Скачать файлы с ftp сама по себе задача не сложная, но путём недолгих экспериментов было выяснено, что скачивание файлов занимает время, а таймаут ftp-соединения приходит к нам гораздо быстрее. Следовательно, качать нужно каждый файл в новом соединении, иначе велик риск чего-то потом не досчитаться в скачанных файлах.

Для этого нам нужен список этих самых файлов. Ни о каком статичном списке файлов, конечно, речи не идет, значит нам его при каждом выполнении скрипта получать с сервера по-новой.

Удобства ради и чтобы не таскать параметры по всему коду - переопределим параметры стандартного класса ftp:

class MyFtp (ftplib.FTP):
    """Класс переопределяет стандартный, чтобы задать все параметры соединение в одном месте"""
    def __init__(self):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.timeout = 1800
        super(MyFtp, self).__init__()

    def connect(self):
        super(MyFtp, self).connect(self.host, timeout=self.timeout)

    def login(self):
        super(MyFtp, self).login(user=self.user, passwd=self.passwd)

    def quit(self):
        super(MyFtp,self).quit()
Параметры берутся из конфига. Конечно же в нужно не забыть импортировать библиотеку ftplib, чтобы этот кусок заработал.

Список файлов с сервера мы получим с помощью следующего класса:

class FileList:
    """Класс для работы со списком загружаемых файлов"""
    def __init__(self):
        self.ftp = None
        self.file_list = []

    def connect_ftp(self):
        import sys
        self.ftp = MyFtp()
        self.ftp.connect()
        self.ftp.login()
        self.ftp.__class__.encoding = sys.getfilesystemencoding()

    def get_list(self, name):
        """Метод для получения списка всех файлов с ftp-сервера."""
        import os
        for dirname in self.ftp.mlsd(str(name), facts=["type"]):
            if dirname[1]["type"] == "file":
                entry_file_list = {}
                entry_file_list['remote_path'] = name  #путь до файла
                entry_file_list['filename'] = dirname[0]  #имя файла
                self.file_list.append(entry_file_list)
            else:
                path = os.path.join(name, dirname[0])
                self.get_list(path)

    def get_next_file(self):
        return self.file_list.pop()

    def len(self):
        return len(self.file_list)
Помимо методов соединения с сервером, получения списка файлов и определения его длины здесь имеет метод, который возвращает нам следующий файл для скачивания, из списка он при этом, конечно, удаляется.

Логирование
Для ведения логов скачивания будет использовать стандартную библиотеку logging. Создадим класс, который будет заниматься логированием.

class MyLogger:
    """Класс для логирования событий"""
    def __init__(self):
        self.logger = None

    def start_file_logging(self, logger_name, log_path):
        """Обычное логирование в файл"""
        import logging
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        try:
            fh = logging.FileHandler(log_path)
        except FileNotFoundError:
            log_path = "downloader.log"
            fh = logging.FileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def start_rotate_logging(self, logger_name, log_path, max_bytes=104857600, story_backup=5):
        """Логирование в файл с ротацией логов"""
        import logging
        from logging.handlers import RotatingFileHandler
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        try:
            fh = RotatingFileHandler(log_path, maxBytes=max_bytes, backupCount=story_backup)
        except FileNotFoundError:
            log_path = "downloader.log"
            fh = RotatingFileHandler(log_path, maxBytes=max_bytes, backupCount=story_backup)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def add(self, msg):
        self.logger.info(str(msg))

    def add_error(self, msg):
        self.logger.error(str(msg))
Скрипт будет поддерживать просто логирование в файл и ротацию файловых логов, ибо логи имеют свойство расти непомерно и это надо бы держать под контролем.

Скачивание файла
Каждый файл будет скачиваться в отдельном потоке. Класс, скачивающий один конкретный файл с сервера выглядит следующим образом:

class BaseFileDownload(threading.Thread):
    """ Объект для копируемого файла """
    count = 0

    def __init__(self, rpath, filename, log):
        threading.Thread.__init__(self)
        self.remote_path = rpath
        self.filename = filename
        self.ftp = None
        self.command = None
        self.currentpath = None
        self.log = log
        self.__class__.count += 1 # для подсчета одновременно запущенных закачек

    def __del__(self):
        self.__class__.count -= 1

    def connect(self):
        """Метод для соединения с ftp"""
        import sys
        self.ftp = MyFtp()
        self.ftp.connect()
        self.ftp.login()
        self.ftp.__class__.encoding = sys.getfilesystemencoding()


    def run(self):
        """Запуск потока скачивания"""
        import os
        self.connect()
        self.command = str(bytes('RETR ', encoding='latin-1'), encoding='utf-8')
        self.currentpath = os.path.join(basepath, self.remote_path[3:])
        self.ftp.cwd(self.remote_path)
        if not os.path.exists(self.currentpath):
            os.makedirs(self.currentpath, exist_ok=True)
        self.host_file = os.path.join(self.currentpath, self.filename)
        try:
            with open(self.host_file, 'wb') as local_file:
                self.log.add("Start downloading " + self.filename)
                self.ftp.retrbinary(self.command + self.filename, local_file.write)
                self.log.add("Downloading " + self.filename + " complete")
        except ftplib.error_perm:
            self.log.add_error('Perm error')
        self.ftp.quit()
Для подсчета количества одновременно скачиваемых файлов мы будет использовать свойство класса count. В нём у нас будет количество существующих экземпляров класса: в конструкторе счетчик наращивается, в деструкторе, соответственно, уменьшается.

Метод для запуска скачивания должен обязательно называться run - это требование библиотеки threading (не забываем её импортировать!), которую мы будем использовать для параллельного запуска нескольких процессов скачивания.

При сохранении списка файлов скрипт сохраняет также путь до этого файла, этот путь мы воссоздаем при скачивании с помощью os.makedirs.

Статус-файл
По завершению скачивания скрипт будет записывать в файл уведомление об этом. Это уведомление можно мониторить zabbix, чтобы понимать когда бэкап не отработал или, как сделал я - написать простого бота, чтобы периодически проверять статус.

Класс для работы с этим файлов выглядит так:

class StatusFile:
    """По окончанию задачи скрипт пишет в файл уведомление о корректном выполнении."""
    def __init__(self):
        self.msg = ''

    def setstatus(self, msg):
        global statusfilepath
        with open(statusfilepath, 'w') as status_file:
            status_file.write(msg)
Многопоточность
Ну и, наконец, сама основная функция скрипта, которая осуществляет работу с потоками скачивания:

def main():
    import os
    import datetime
    import time

    log = MyLogger()
    log.start_rotate_logging("DownloaderLog", os.path.join(log_path, "download_backup.log")) # запускаем логирование
    now = datetime.datetime.today().strftime("%Y%m%d")
    global basepath
    basepath = os.path.join(basepath, now)  # модифицируем путь, добавляя текущую дату
    list_file = FileList()
    list_file.connect_ftp()
    list_file.get_list("..")
    for i in range(list_file.len()):
        flag = True
        while flag:   # цикл внутри которого поддерживается нужное количество одновременно запущенных загрузок
            if BaseFileDownload.count < max_threads:
                curfile = list_file.get_next_file()
                threadid = BaseFileDownload(curfile["remote_path"], curfile["filename"], log)
                threadid.start()
                flag = False
            else:
                time.sleep(20)
    log.add("Downloading files complete")
    statusfile = StatusFile()
    statusfile.setstatus("Downloading at " + str(datetime.datetime.now()) + " finishing successful")
Здесь мы запускаем логирование, получаем список файлов ( он хранится в памяти).

В вечном цикле while мы проверяем количество одновременно запущенных скачиваний и, при необходимости, запускаем дополнительные потоки.

Исходный код целиком можно найти здесь.
"https://github.com/kit567/ftpmultithreaddownloader.git"

=====================================================================================================

Dair_Targ
"https://github.com/aio-libs/aioftp"
Для подобных операций в питоне asyncio зачастую на порядок быстрее многопоточности при существенно меньшем потреблении ресурсов.

Sun_123
Несмотря на утверждение автора "увы, ничего готового работающего так же быстро для моих условий найти не удалось" у меня есть приложение, написанное на асинкио (поскольку он лучше подходит для большого числа I/O_операций, да): 
"github.com/Sunlight-Rim/FTPSearcher"

Оно индексирует файлы и сохраняет в список, но там парой строчек автор мог бы добавить функцию скачивания. Однако статья энивей познавательная.

Dasdy
Если хочется всё-таки написать что-то своё, то есть несколько замечаний:
1) Не смотрели в сторону "ThreadPoolExecutor"?
"https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor"
Вручную управлять полноценными потоками — неблагодарное занятие, довольно много граблей. Должно упростить код и избавить от некоторых проблем, которые могут внезапно сейчас возникнуть (например, глобальный доступ всех потоков к переменной thread_count, еще и каждый поток её менять может*)
2) Так как у вас написана обёртка FTP, вы не сможете её использовать как контекстный менеджер. Это в целом еще ладно, но с таким подходом надо следить за правильным закрытием клиента — например, если при получении файла вылетит любая ошибка, кроме error_perm
3) Обычно принято называть методы get_* тогда, когда они что-нибудь да возвращают. В целом, логичнее было бы его вообще спрятать внутри класса, и вызывать только при вызове get_next_file (который можно сделать генератором)
* Не используйте __del__, по возможности, никогда. Вы не контролируете момент, когда обьект будет удаляться.

a-l-e-x
я не очень большой специалист…
что произойдёт, если соединение (или много соединений) разрывается (по любой причине) в процессе скачивания?
можно ли один (например большой) файл скачивать параллельно (одновременно в несколько потоков)?
что произойдёт, в случае ошибки в основном скрипте (цикле), а не в скачивающем потоке?

gecube
Да тут даже веселее — если в процессе скачивания появляются новые файлы или изменяются уже существующие, то приплыли?

reijii567
Глобально вы правы, но конкретно в моей ситуации такое не может произойти, потому не предусмотрено.

Sergey_datex
По логике многопоточное копирование всегда медленней однопоточного (в масштабах, к примеру, одного ПК). При многопотоке дисковой подсистеме приходится одновременно отрабатывать запись/чтение из разных мест носителя, что суммарно медленней последовательного копирования тех же файлов. В чем преимущество многопоточности в FTP? Изначально ограничения в скорости одного потока? Тогда нужно копать в сторону устранения этого узкого места.

pansa
Во всех актуальных ОС (почти)весь io кэшируется в памяти.
ssd решает =)

Sergey_datex
1) вы все равно упретесь в дисковую подсистему. Сколько не кешируй, но данные нужно будет сбрасывать на диск. Если пишешь в 10 потоков — проиграешь в сумме.
2) в цепочке vps-комп автора, да и с оглядкой на объем бекапа (500 гиг) с большой вероятностью есть обычный HDD.

gecube
Не согласен. Во многих случаях не дисковая подсистема является узким местом, а сам протокол фтп или сеть.

pansa
Ну, понятно, можно специально собрать из барахла очень тормозной массив, а сеть поднять 10GE, но мы же говорим о вменяемых конфигурациях. Если сервер удаленный, а не в локалке, то наиболее вероятно именно затыки сети будут батлнеком.
"обычный" современный hdd выдаст 80-100мб/с линейной записи, к которой как раз будет стремиться процесс сброса кэша. Я был бы рад, если бы мой бэкап с удалённого хоста упирался не в сеть, а в 80мб/с локальной записи =)

ilyakruchinin
lftp и не нужно никакое велосипедостроение
Документация: https://lftp.yar.ru/lftp-man.html

S0mbre
Уже отмечали, но все же — мои 5 копеек:
1) Гораздо лучше использовать вместо самописного пула потоков готовое решение на python: самое простое — это "Pool из пакета multiprocessing".
"https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool"

По умолчанию, многозадачность реализована за счет параллельных процессов, что лучше, чем потоки, т.к. не накладывает ограничений на ядра процессора. А еще лучше — Dask, который позволяет делать намного больше!
2) Зачем использовать FTP.retrbinary, передавая в callback метод write файлового потока, когда гораздо эффективнее сразу использовать FTP.storbinary, который сразу сохраняет блоки данных в указанный поток? Сигнатура метода:
FTP.storbinary(cmd, fp, blocksize=8192, callback=None, rest=None)

Т.е. вы можете в callback теперь передавать свою процедуру для отслеживания самого процесса скачивания (например, перерисовка progressbar в каком-то интерфейсе или возможность ранней отмены ненужной закачки). А то у вас только можно отследить начало и конец скачивания файла.
3) Ну и наконец… А нужен ли python для этого? Я имею в виду, чисто скачивать с сервера файлы и писать лог. Честно, я бы поискал и нашел какой-то готовый клиент с поддержкой нужного функционала.

VD42
STOR — это закачать файл на сервер.
Только полноправные пользователи могут оставлять комментарии. Войдите, пожалуйста.

