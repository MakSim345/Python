Вывод в файлы:

file = open('data.txt', 'w')

Если полный путь к файлу не указан, то файл будет создан в текущем рабочем каталоге.
Если в этом каталоге уже существует такой файл, то он будет удален и создан новый.
С режимом "w" нужно быть осторожнее, можно потерять содержимое старого файла.


myfile = open("C:\\projects\\data.txt", "w")
myfile.write("# Name Email Phone\n")
myfile.write("Larry larry@example.com 111-1111\n")
myfile.write("Curly curly@example.com 222-2222\n")
myfile.write("Moe moe@example.com 333-3333\n")
myfile.close()


c:\projects>type data.txt
# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333

c:\projects>

В отличии от функции print, метод write объекта файла записывает в точности то, 
что ему передано, без дополнительного форматирования.
Поэтому мы явно добавляем символ конца строки.

Метод close завершает формирование содержимого файла и освобождает системные ресурсы.
Обычно файлы автоматически закрываются, когда объект файла уничтожается 
интерпретатором при сборке мусора (т.е. когда в сценарии исчезнет послдняя ссылка на объект)

В случае использования временных файлов, метод close можно и не применять:

open('tempfile.txt','w').write("Scott Tiger\n")
open('tempfile.txt','r').read()


Гарантированное закрытие файлов:

- Использовать обработчик исключений

myfile = open("C:\\projects\\data.txt", "w")
try:
    myfile.write("# Name Email Phone\n")
    myfile.write("Larry larry@example.com 111-1111\n")
    myfile.write("Curly curly@example.com 222-2222\n")
    myfile.write("Moe moe@example.com 333-3333\n")
finally:
    myfile.close()


c:\projects>type data.txt
# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333

- использовать менеджер контекста

Инструкция with - обеспечивает  более краткий способ реализации заключительных 
операций для объектов определенных типов, включая закрытие файлов.

with open("C:\\projects\\data.txt", "w")  as myfile:
    # обработка файла
    myfile.write("# Name Email Phone\n")
    myfile.write("Larry larry@example.com 111-1111\n")
    myfile.write("Curly curly@example.com 222-2222\n")
    myfile.write("Moe moe@example.com 333-3333\n")
    # закрывается автоматически после выхода
    # независимо от возникновения исключений

c:\projects>type data.txt
# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333

В версии Python 3.1 появились вложенные менеджеры контекста:

with A() as a, B() as b:
    # инструкции

при выходе из этой конструкции автоматически закроются оба файла, независимо от того,
возникло исключение или нет.

Это действует так:
with A() as a:
    with B() as b:
        # инструкции


Например:

with open("C:\\projects\\data.txt") as fin, open("C:\\projects\\data1.txt", 'w') as fout:
    for line in fin:
        fout.write(line.upper())

C:\Users\angor>cd c:\projects

c:\projects>type data.txt
# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333

c:\projects>type data1.txt
# NAME EMAIL PHONE
LARRY LARRY@EXAMPLE.COM 111-1111
CURLY CURLY@EXAMPLE.COM 222-2222
MOE MOE@EXAMPLE.COM 333-3333

c:\projects>

Для записи в файлы можно также использовать метод writelines, 
который просто записывает все строки из списка без дополнительного форматирования.

myfile = open("C:\\projects\\data.txt", "w")
myfile.writelines(["# Name Email Phone\n",
                  "Larry larry@example.com 111-1111\n",
                  "Curly curly@example.com 222-2222\n",
                  "Moe moe@example.com 333-3333\n"])
myfile.close()

C:\Users\angor>cd c:\projects

c:\projects>type data.txt
# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333

Такой метод может эмулироваться циклом for и его удобно использовать в сценариях, 
которые сначала сохраняют выходные данные в списке, а потом записывают этот список в файл.


Чтение из файлов:

file = open('data.txt', 'r')

режим r используется по умолчанию, поэтому можем писать так:

file = open('data.txt')


пример:

myfile = open("C:\\projects\\data.txt")
lines = myfile.readlines()
for line in lines:
    print(line, end='')


# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333


Метод readlines загружает содержимое файла в память целиком 
и передает его сценарию в виде списка строк, который можно обойти в цикле.

Существует много способов чтения вхлдного файла:

file.read()
возвращает строку, содержащую все символы (или байты), хранящиеся в файле.


file.read(N)
возвращает строку, содержащую очередные N символов (или байтов), из файла.


file.readline()
читает содержимое файла до ближайшего символа \n и возвращает строку.


file.readlines()
читает файл целиком и возвращает список строк


Вызов метода seek(0) перед каждой попыткой чтения переустанавливает текущую позицию чтения в начало файла.

Python 3.3.1 (v3.3.1:d9893d13c628, Apr  6 2013, 20:30:21) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> myfile = open("C:\\projects\\data.txt")
>>> myfile.seek(0)
0
>>> myfile.read()
'# Name Email Phone\nLarry larry@example.com 111-1111\nCurly curly@example.com 222-2222\nMoe moe@example.com 333-3333\n'


>>> myfile.seek(0)
0
>>> myfile.readlines()
['# Name Email Phone\n', 'Larry larry@example.com 111-1111\n', 'Curly curly@example.com 222-2222\n', 'Moe moe@example.com 333-3333\n']


>>> myfile.seek(0)
0
>>> myfile.readline()
'# Name Email Phone\n'

>>> myfile.readline()
'Larry larry@example.com 111-1111\n'

>>> myfile.readline()
'Curly curly@example.com 222-2222\n'

>>> myfile.readline()
'Moe moe@example.com 333-3333\n'

>>> myfile.readline()
''

>>> myfile.readline()
''


>>> myfile.seek(0)
0
>>> myfile.read(1)
'#'
>>> 
>>> myfile.read(8)
' Name Em'



>>> myfile.seek(0)
0
>>> myfile.read(1), myfile.read(8)
('#', ' Name Em')
>>> 



Методы read() и readlines() загружают в память сразу весь файл.
Их можно использовать при работе с небольшими файлами.

Для работы с потенциально большими файлами необходимо использовать вызовы

readline() и read(N)

Оба метода возвращают пустую строку по достижении конца файла.

seek(0) - означает вернуться в начало файла
это альтернатива повторному открытию файла перед очередной попыткой чтения из него.


Чтение строк с помощью итераторов файлов

В старых версиях Python принято было читать файл в список и одход этого списка в цикле:

myfile = open("C:\\projects\\data.txt")
for line in myfile.readlines():
    print(line, end='')

# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333

Больше не делайте так никогда !!!

В новых версиях Python объект файла включает итератор, 
который при каждом обращении извлекает только одну строку из файла.

Теперь нет необходимости вызывать метод readlines.

myfile = open("C:\\projects\\data.txt")
for line in myfile:
    print(line, end='')


# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333


Более того теперь файл можно открывать непосредственно в инструкции цикла, 
как временный, который будет автоматически закрыт после выхода из цикла:

for line in open("C:\\projects\\data.txt"):
    print(line, end='')


# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333


Это наиболее предпочтительный способ чтения из файла на сегодняшний день.


Вообще итератор это всего лишь метод

__next__ , вызываемый встроенной функцией next.

Он своим поведением напоминает метод readline, за исключением того , 
что по достижении конца файла методы чтения возвращают пустую строку, 
а итератор возбуждает исключение, чтобы прервать итерации.

Python 3.3.1 (v3.3.1:d9893d13c628, Apr  6 2013, 20:30:21) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> myfile = open("C:\\projects\\data.txt")
>>> myfile.readline()
'# Name Email Phone\n'
>>> myfile.readline()
'Larry larry@example.com 111-1111\n'
>>> myfile.readline()
'Curly curly@example.com 222-2222\n'
>>> myfile.readline()
'Moe moe@example.com 333-3333\n'
>>> myfile.readline()
''
>>> 
>>> 
>>> 
>>> myfile = open("C:\\projects\\data.txt")
>>> myfile.__next__()
'# Name Email Phone\n'
>>> myfile.__next__()
'Larry larry@example.com 111-1111\n'
>>> myfile.__next__()
'Curly curly@example.com 222-2222\n'
>>> myfile.__next__()
'Moe moe@example.com 333-3333\n'
>>> myfile.__next__()
Traceback (most recent call last):
  File "", line 1, in 
    myfile.__next__()
StopIteration
>>> 


Интересно отметить, что итераторы автоматически используются во всех итерационных контекстах, 
включая конструктор списка, генераторы списков, функцию map и оператор in проверки на вхождение:

>>> open("C:\\projects\\data.txt").readlines()
['# Name Email Phone\n', 'Larry larry@example.com 111-1111\n', 'Curly curly@example.com 222-2222\n', 'Moe moe@example.com 333-3333\n']
>>> 
 
>>> list(open("C:\\projects\\data.txt"))
['# Name Email Phone\n', 'Larry larry@example.com 111-1111\n', 'Curly curly@example.com 222-2222\n', 'Moe moe@example.com 333-3333\n']
>>> 

>>> lines=[line.rstrip() for line in open("C:\\projects\\data.txt")]
>>> lines
['# Name Email Phone', 'Larry larry@example.com 111-1111', 'Curly curly@example.com 222-2222', 'Moe moe@example.com 333-3333']
>>> 

>>> lines=[line.upper() for line in open("C:\\projects\\data.txt")]
>>> lines
['# NAME EMAIL PHONE\n', 'LARRY LARRY@EXAMPLE.COM 111-1111\n', 'CURLY CURLY@EXAMPLE.COM 222-2222\n', 'MOE MOE@EXAMPLE.COM 333-3333\n']
>>> 

>>> list(map(str.split, open("C:\\projects\\data.txt")))
[['#', 'Name', 'Email', 'Phone'], ['Larry', 'larry@example.com', '111-1111'], ['Curly', 'curly@example.com', '222-2222'], ['Moe', 'moe@example.com', '333-3333']]
>>> 

>>> line = '# Name Email Phone\n'
>>> line in open("C:\\projects\\data.txt")
True
>>> 


Примеры:

Чтение строк из файла и вывод их с помощью функции print:


f = open("C:\\projects\\data.txt", "r")
while True:
    theline = f.readline()
    if len(theline) == 0:
        break
    print(theline, end="")
f.close()

# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333


Чтение строк из файла, сортировка их в памяти и запись в другой файл:

fin = open("C:\\projects\\data.txt", "r")
buf = fin.readlines()
fin.close()
buf.sort()
fout = open("C:\\projects\\data1.txt", "w")
for line in buf:
    fout.write(line)
    print(line)
fout.close()

# Name Email Phone
Curly curly@example.com 222-2222
Larry larry@example.com 111-1111
Moe moe@example.com 333-3333

Чтение строк из файла, создание списка слов из этого файла, и вывод количества слов: 

f = open("C:\\projects\\data.txt")
content = f.read()
f.close()
words = content.split()
print(words)
print("There are {0} words in the file.".format(len(words)))


['#', 'Name', 'Email', 'Phone', 'Larry', 'larry@example.com', '111-1111', 'Curly', 'curly@example.com', '222-2222', 'Moe', 'moe@example.com', '333-3333']

There are 13 words in the file.


Пример работы с бинарными файлами:

fin  = open("C:\\projects\\data.txt", "rb")
fout = open("C:\\projects\\data2.txt", "wb")
while True:
    buf = fin.read(1024)
    if len(buf) == 0:
        break
    fout.write(buf)
fin.close()
fout.close()


c:\projects>type data2.txt
# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333



Считать все строки из одного файла и записать все строки кроме тех, 
которые начинаются на "#" в другой файл:


def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if text[0] == "#":
            continue
        outfile.write(text)
    infile.close()
    outfile.close()

filter("C:\\projects\\data.txt","C:\\projects\\data3.txt")

c:\projects>type data3.txt
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333


Считать все строки из файла в список.
Вывести первые два элемента списка (первые две строки):

wordsfile = open("C:\\projects\\data.txt", "r")
wordlist = wordsfile.readlines()
print(wordlist[:2])


['# Name Email Phone\n', 'Larry larry@example.com 111-1111\n']


Другие режимы открытия файлов

Помимо режимов "r" и "w" большинство платформ поддерживает режим "a"

a - append

 При этом вызов функции open не уничтожает текущее содержимое файла, а методы записи добавляют данные в конец файла.


myfile = open("C:\\projects\\data.txt", "w")
myfile.write("# Name Email Phone\n")
myfile.write("Larry larry@example.com 111-1111\n")
myfile.close()
print(open("C:\\projects\\data.txt").read())
myfile.close()


# Name Email Phone
Larry larry@example.com 111-1111


myfile = open("C:\\projects\\data.txt", "a")
myfile.write("Curly curly@example.com 222-2222\n")
myfile.write("Moe moe@example.com 333-3333\n")
myfile.close()
print(open("C:\\projects\\data.txt").read())
myfile.close()


# Name Email Phone
Larry larry@example.com 111-1111
Curly curly@example.com 222-2222
Moe moe@example.com 333-3333


Чаще всего функцию open используют так:

open(имя_файла, режим_открытия, размер_буфера)

обязательный только первый аргумент

По умолчанию:

режим открытия  r
буферизация     полная


Режимы открытия:


r+
файл доступен как для чтения так и для записи, при этом содержимое существующих файлов сохраняется.

w+
файл доступен как для чтения так и для записи, при этом создается файл заново, уничтожая прежнее его содержимое.


rb
читать файл в двоичном режиме

wb
записывать файл в лвоичном режиме


rb+
файл доступен как для чтения так и для записи в двоичном режиме, при этом содержимое существующих файлов сохраняется.

wb+                                                           
файл доступен как для чтения так и для записи в двоичном режиме, при этом создается файл заново, уничтожая прежнее его содержимое.


Проще говоря, по умолчанию используется режим для чтения r, но вы можете использовать режим
w - для записи
a - для дополнения

Можете добавлять символ + , чтобы обеспечить возможность изменения содержимого файла,
а также указывать b и t  чтобы задать двоичный или текстовый режим.

Размер буфера

Функция open принимает необязятельный третий аргумент с размером буфера

0 
отсутствие буферизации, данные передаются немедленно,
это значение допустимо только для двоичных режимов

1
построчная буферизация

Любое другое положительное число означает использование режима полной буферизации
этот режим используется по умолчанию


Двоичные и текстовые файлы

Двоичные файлы:

- изображения JPEG
- аудиоклипы
- упакованные двоичные данные


открыть двоичный файл для записи
myfile = open("C:\\projects\\data.txt", "wb")

открыть двоичный файл для чтения
myfile = open("C:\\projects\\data.txt", "rb")

Далее можно использовать стандартные методы:

read
write

Методы readline и readlines как и построчные итераторы файлов, 
по прежнему будут работать с текстовыми файлами, открытыми в двоичном режиме.
Но нет никакого смысла применять их к действительно двоичным данным, которые не имеют построчной организации.
(байты \n никакого смысла там не имеют и их может вообще не быть)

Python 3.3.1 (v3.3.1:d9893d13c628, Apr  6 2013, 20:30:21) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> open("C:\\projects\\data.txt").read()
'# Name Email Phone\nLarry larry@example.com 111-1111\nCurly curly@example.com 222-2222\nMoe moe@example.com 333-3333\n'
>>> 

>>> open("C:\\projects\\data.txt", "rb").read()
b'# Name Email Phone\r\nLarry larry@example.com 111-1111\r\nCurly curly@example.com 222-2222\r\nMoe moe@example.com 333-3333\r\n'
>>> 
>>> 


>>> myfile = open("C:\\projects\\data.txt", "rb")
>>> for line in myfile:
    print(line)

    
b'# Name Email Phone\r\n'
b'Larry larry@example.com 111-1111\r\n'
b'Curly curly@example.com 222-2222\r\n'
b'Moe moe@example.com 333-3333\r\n'
>>> 
>>> 


>>> open("C:\\projects\\data.bin", 'wb').write(b'# Name Email Phone\n')
19

>>> open("C:\\projects\\data.bin", 'rb').read()
b'# Name Email Phone\n'
>>> 
>>> 


>>> open("C:\\projects\\data.bin", 'wb').write('# Name Email Phone\n')
Traceback (most recent call last):
  File "", line 1, in 
    open("C:\\projects\\data.bin", 'wb').write('# Name Email Phone\n')
TypeError: 'str' does not support the buffer interface
>>> 
аргумент должен быть типа bytes


Кодирование символов Unicode в текстовых файлах

>>> data = 'sp\xe4m'
>>> data
'späm'
>>> 
>>> 0xe4, bin(0xe4), chr(0xe4)
(228, '0b11100100', 'ä')
>>> 

Закодируем эту строку вручную

>>> data = 'sp\xe4m'
>>> data
'späm'
>>> 


>>> 0xe4, bin(0xe4), chr(0xe4)
(228, '0b11100100', 'ä')
>>> 


>>> data.encode('latin1')
b'sp\xe4m'
>>> 


>>> data.encode('utf8')
b'sp\xc3\xa4m'
>>> 


>>> data.encode('ascii')
Traceback (most recent call last):
  File "", line 1, in 
    data.encode('ascii')
UnicodeEncodeError: 'ascii' codec can't encode character '\xe4' in position 2: ordinal not in range(128)
>>> 


>>> data.encode('utf-16')
b'\xff\xfes\x00p\x00\xe4\x00m\x00'
>>> 


>>> data.encode('cp500')
b'\xa2\x97C\x94'
>>> 


>>> open("C:\\projects\\data.txt", 'w', encoding='latin1').write(data)
4

>>> open("C:\\projects\\data.txt", 'r', encoding='latin1').read()
'späm'
>>> 


>>> open("C:\\projects\\data.txt", 'rb').read()
b'sp\xe4m'
>>> 


>>> open("C:\\projects\\data.txt", 'w', encoding='utf8').write(data)
4
>>> 


>>> open("C:\\projects\\data.txt", 'r', encoding='utf8').read()
'späm'
>>> 


>>> open("C:\\projects\\data.txt", 'rb').read()
b'sp\xc3\xa4m'>>> 


>>> open("C:\\projects\\data.txt", 'w', encoding='ascii').write(data)
Traceback (most recent call last):
  File "", line 1, in 
    open("C:\\projects\\data.txt", 'w', encoding='ascii').write(data)
UnicodeEncodeError: 'ascii' codec can't encode character '\xe4' in position 2: ordinal not in range(128)
>>> 


>>> open(r'C:\Python33\python.exe', 'r').read()
Traceback (most recent call last):
  File "", line 1, in 
    open(r'C:\Python33\python.exe', 'r').read()
  File "C:\Python33\lib\encodings\cp1251.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 16964: character maps to 
>>> 


>>> open("C:\\projects\\data.txt", 'w', encoding='cp500').writelines(['spam\n', 'ham\n'])

>>> open("C:\\projects\\data.txt", 'r', encoding='cp500').readlines()
['spam\n', 'ham\n']
>>> 


>>> open("C:\\projects\\data.txt", 'r').readlines()
['ў—Ѓ”\n', '%€Ѓ”\n', '%']
>>> 


>>> open("C:\\projects\\data.txt", 'rb').readlines()
[b'\xa2\x97\x81\x94\r%\x88\x81\x94\r%']
>>> 


>>> open("C:\\projects\\data.txt", 'rb').read()
b'\xa2\x97\x81\x94\r%\x88\x81\x94\r%'
>>>

Имейте ввиду, что текст в кодированном двоичном представлении не может обрабатываться так, как вам хотелось бы.
Текст, закодированный с применением определенной кодировки, не может сравниваться или объединяться с текстом,
закодированным с применением других кодировок.

Преобразование символов конца строки в Windows

Конец строки текста в файле:

\n     в Unix и Linux

\r\n   в Windows


В Python объекты файлов автоматически отображают последовательность DOS \r\n в одиночный символ \n

При выполннии сценариев в Windows:

- для файлов открытых в текстовом режиме, при чтении \r\n преобразуется в \n
  при записи \n  преобразуется в \r\n

- для файлов открытых в двоичном режиме никакие преобразования не производятся.

В UNIX - подобных системах преобразование не производится в любом режиме, т.к. там используется \n

Python скрипт всегда работает с \n
Просто во внешних файлах на платформе Windows он преобразует конец строки в \r\n

Поэтому если на платформе Windows вы ошибочно откроете двоичный файл в текстовом режиме, 
то при сохранении вы можете повредить файл, если в файле  случайно втретился символ \n
вы его перезапиите в \r\n
а при чтении \r\n  символ  \r  будет отброшен


>>> open("C:\\projects\\data.txt", 'w').write('shrubbery\n')
10
>>>
\n  преобразован в \r\n


>>> open("C:\\projects\\data.txt", 'rb').read()
b'shrubbery\r\n'
>>> 
>>> open("C:\\projects\\data.txt", 'r').read()
'shrubbery\n'
>>> 
>>> data = b'a\0b\rc\r\nd'      # 4 байта 4 обычных символа
>>> len(data)
8
>>> 

Запись двоичных данных
>>> open("C:\\projects\\data.bin", 'wb').write(data)
8
>>> 

Чтение двоичных данных
>>> open("C:\\projects\\data.bin", 'rb').read()
b'a\x00b\rc\r\nd'
>>> 
0 - отобразился как шестнадцатеричная последовательность x00


Попробуем прочитать в текстовом режиме:
>>> open("C:\\projects\\data.bin", 'r').read()
'a\x00b\nc\nd'
>>> 

символы \r - искажены

При записи двоичных данных в текстовом режимемогут изменяться или вставляться байты, 
значения которых совпадают с символами конца строки
(если данные успешно пройдут этап кодирования в кодировку по умолчанию)

>>> open("C:\\projects\\data.bin", 'w').write(data)
Traceback (most recent call last):
  File "", line 1, in 
    open("C:\\projects\\data.bin", 'w').write(data)
TypeError: must be str, not bytes
>>> 

В текстовом режиме должна передаваться строка типа str
Используйте  bytes.decode() для преобразования типа.

>>> data.decode()
'a\x00b\rc\r\nd'
>>> open("C:\\projects\\data.bin", 'w').write(data.decode())
8
>>> 


>>> open("C:\\projects\\data.bin", 'rb').read()
b'a\x00b\rc\r\r\nd'
>>> 
запись в текстовом режиме добавила символ \r


>>> open("C:\\projects\\data.bin", 'r').read()
'a\x00b\nc\n\nd'
>>> 
опять символы \r искажены


Произвольный доступ к данным в файлах

При открытии файлов текущая позиция обычно устанавливается в смещение 0 от начала файла 
и перемещается вперед по мере чтения/записи данных.

Метод seek позволяет переместить текущую позицию для следующей операции чтения/записи в другое место, 
для чего ему достаточно передать величину смещения в байтах.

seek(n)

seek(n, mode)

mode = 0 абсолютное смещение на n байтов (по умолчанию)
mode = 1 смещение относительно текущей позиции на n байтов
mode = 2 смещение относительно конца файла на n байтов


seek(0)  - перемотать файл в начало (rewind) т.е. текущую позицию переместить в начало файла.


>>> records = [bytes([char]*8) for char in b'mars']
>>> records
[b'mmmmmmmm', b'aaaaaaaa', b'rrrrrrrr', b'ssssssss']
>>> 
 

>>> myfile = open("C:\\projects\\random.bin", "w+b")
>>> for rec in records:
    size = myfile.write(rec) # записать 4 записи

    
>>> myfile.flush()
>>> pos = myfile.seek(0)    # прочитать файл целиком

>>> print(myfile.read())
b'mmmmmmmmaaaaaaaarrrrrrrrssssssss'
>>> 


Теперь повторно откроем файл в режиме r+b 
он также позволяет читать из файла и писать в него,
но не очищает файл при открытии.

>>> myfile = open("C:\\projects\\random.bin", "r+b")
>>> print(myfile.read())    # прочитать файл целиком
b'mmmmmmmmaaaaaaaarrrrrrrrssssssss'
>>> 
 
>>> record = b'X' * 8
>>> myfile.seek(0)
0
>>> 
 
>>> myfile.write(record)         # изменим первую запись
8
>>> 
 
>>> myfile.seek(len(record)*2)
16
>>> 
 
>>> myfile.write(b'Y' * 8)       # изменим 3-ю запись
8
>>> 
 
>>> myfile.seek(8)
8
>>> 
 
>>> myfile.read(len(record))     # извлечем 2-ю запись
b'aaaaaaaa'
>>> 
 
>>> myfile.read(len(record))     # извлечем следующую (3-ю) запись
b'YYYYYYYY'
>>> 
 
>>> myfile.seek(0)
0
>>> 
 
>>> myfile.read()                # прочитать файл целиком
b'XXXXXXXXaaaaaaaaYYYYYYYYssssssss'
>>> 


C:\projects>type random.bin
XXXXXXXXaaaaaaaaYYYYYYYYssssssss 





Метод seek можно использовать, даже если файл открыт только для чтения.

Пример:

Чтение произвольных записей фиксированной длины.
Используем текстовый режим r
Данные представляют простой текст ASCII, где каждый символ представлен одним байтом
и текст не содержит символов конца строки.

>>> myfile = open("C:\\projects\\random.bin", "r")
>>> 

>>> reclen = 8
>>> 

>>> myfile.seek(reclen * 3)
24

>>> myfile.read(reclen)         # извлечь 4-ю запись
'ssssssss'
>>> 

>>> myfile.seek(reclen * 1)
8

>>> myfile.read(reclen)         # извлечь 2-ю запись
'aaaaaaaa'
>>> 


Двоичный режим с таким файлом работает также:

>>> myfile = open("C:\\projects\\random.bin", "rb")
>>> 

>>> myfile.seek(reclen * 2)
16

>>> myfile.read(reclen)
b'YYYYYYYY'
>>>


В общем случае текстовый режим не следует использовать, если вам требуется произвольный доступ к записям
(за исключением файлов с простым некодируемым текстом, подобным ASCII, не содержащим символов конца строки)

Пример:

Соответствие между строкой Python и ее кодированным представлением в файле нарушается сразу же за первым не ASCII символом:


>>> data = 'sp\xe4m'

>>> data, len(data)
('späm', 4)

>>> data.encode('utf-8'), len(data.encode('utf-8'))
(b'sp\xc3\xa4m', 5)

Как видим , до кодирования длина строки составляла 4 байта, а после кодирования ее длина стала 5 байтов.
Это существенно осложняет возможность позиционирования по абсолютному смещению.

>>> myfile = open("C:\\projects\\test", mode = "w+", encoding = 'utf8')
>>> 

>>> myfile.write(data)
4
>>> 

>>> myfile.flush()
>>> 

>>> myfile.seek(0); myfile.read(1)
0
's'                                    # для байтов ASCII все OK
>>> 

>>> myfile.seek(2); myfile.read(1)
2
'ä'                                    # двухбайтоый не ASCII
>>> 

>>> data[3]
'm'                                    # а в смещении 3 не "m" !!!
>>> 

>>> myfile.seek(3); myfile.read(1)
3
Traceback (most recent call last):
  File "", line 1, in 
    myfile.seek(3); myfile.read(1)
  File "C:\Python33\lib\codecs.py", line 300, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa4 in position 0: invalid start byte
>>>


Пример:

В файл с переводом английских слов, нужно добавить транскрипцию, взяв ее из другого файла:

list.txt

come - приходить                   
get - получить                     
give - давать                      
go - идти                          
keep - держать                     
let - позволять                    
make - сделать                     
put - поместить                    
seem - казаться                    
take - взять                       
be - быть                          

trans.txt

the [ðə:]
think [θiŋk]
or [ɔ:]
got [gɔt]
good [gud]
eye [ai]
before [bi'fɔ:]
long [lɔŋ]
let [let]
take [teik]
saw [sɔ:]
room [ru:m]
place [pleis]
those [ðəuz]
work [wз:k]
put [put]
 
 with open("C:\\test\\list.txt", "r", encoding='utf-8') as f1, open("C:\\test\\trans.txt", "r", encoding='utf-8') as f2, open("C:\\test\\out.txt", "w", encoding='utf-8') as f3:
    for line1 in f1:
        p1 = line1.split()
        f2.seek(0)
        i=0
        for line2 in f2:
            p2 = line2.split()
            if p2 != []:
                if (p2[0].lower() == p1[0].lower()):
                    f3.write("{0:20} {1:20} {2:3} {3:30}\n".format(p1[0],p2[1],p1[1]," ".join(str(x) for x in p1[2:len(p1)])))
                    i+=1
        if i == 0:
            f3.write("{0:20} {1:20} {2:3} {3:30}\n".format(p1[0],"[]",p1[1]," ".join(str(x) for x in p1[2:len(p1)]))) 






out.txt 
  
come                []                   -   приходить                     
get                  []                   -   получить                      
give                 []                   -   давать                        
go                   []                   -   идти                          
keep                 []                   -   держать                       
let                  [let]                -   позволять                     
make                 []                   -   сделать                       
put                  [put]                -   поместить                     
seem                 []                   -   казаться                      
take                 [teik]               -   взять                         
be                   []                   -   быть                          


Или так:

with open("C:\\test\\list.txt", "r", encoding='utf-8-sig') as f1, open("C:\\test\\trans.txt", "r", encoding='utf-8-sig') as f2, open("C:\\test\\out.txt", "w", encoding='utf-8-sig') as f3:
    for line1 in f1:
        p1 = line1.split()
        f2.seek(0)
        i=0
        for line2 in f2:
            p2 = line2.split()
            if p2 != []:
                if (p2[0].lower() == p1[0].lower()):
                    i+=1
                    if i == 1:
                        f3.write("{0:20} {1:20} {2:3} {3:30}\n".format(p1[0],p2[1],p1[1]," ".join(str(x) for x in p1[2:len(p1)])))
        if i == 0:
            f3.write("{0:20} {1:20} {2:3} {3:30}\n".format(p1[0],"[]",p1[1]," ".join(str(x) for x in p1[2:len(p1)]))) 


