Графический интерфейс на Python за 5 минут

Python легко использовать. В нем вы можете найти огромное количество библиотек для чего угодно. И это его основное преимущество. Из нескольких строк кода вы ничего не сделаете. Если вам нужны скрипты для личного пользования или для технически подкованной аудитории, то вам даже не придется думать о графическом интерфейсе.

Однако иногда ваша целевая аудитория не сильно подкована технически. Люди не против использовать ваши скрипты на Python до тех пор пока им не нужно смотреть на одну строку кода. В таком случае скриптов командной строки будет недостаточно. В идеале вам нужен графический интерфейс. Цель этого поста использовать только Python.

Библиотеки Python, которые можно использовать для графического интерфейса

По сути, есть 3 большие библиотеки Python для графического интерфейса; Tkinter, wxPython и PyQT. Рассматривая их, я не нашел там ничего из того, что мне нравится в Python. Библиотеки Python, как правило, очень хорошо абстрагируются от супер-технических моментов. Если бы мне нужно было работать с объектно-ориентированным программированием, я мог бы с таким же успехом загрузить Java или .Net.

Однако, к счастью, я наткнулся на четвёртый вариант, который был мне по душе. Это PySimpleGUI, я до сих пор ей пользуюсь. Как ни странно, эта библиотека использует все 3 популярные библиотеки, о которых шла речь выше, но при этом абстрагируется от супер технических моментов

Давайте погрузимся в эту библиотеку и изучим ее, одновременно решая реальную проблему.

Проверьте два одинаковых файла

Я рассказал как это сделать в своей статье “3 быстрых способа сравнить данные в Python”. Мы можем использовать первый раздел, проверку целостности данных, чтобы попытаться создать пользовательский интерфейс.

    "3 Quick Ways To Compare Data with Python"
        - "https://medium.com/financeexplained/3-quick-ways-to-compare-data-in-python-65201be10b6"

По факту нам нужно загрузить два файла и выбрать шифрование, которое мы хотели бы использовать для сравнения файлов.

"Запрограммируйте графический интерфейс"

Чтобы создать графический интерфейс, можно использовать этот код:

import PySimpleGUI as sg
layout = [
    [sg.Text('File 1'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('MD5'), sg.Checkbox('SHA1')
     ],
    [sg.Text('File 2'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('SHA256')
     ],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('File Compare', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break

в результате мы получим:

"mage"
# ===============================================# 

"Подключаем логику"

Когда есть пользовательский интерфейс, легко понять, как подключить остальную часть кода. Нам просто нужно следить за тем, что вводит пользователь и действовать соответственно. Мы можем очень легко сделать это с помощью следующего кода:

import PySimpleGUI as sg
import re
import hashlib
def hash(fname, algo):
    if algo == 'MD5':
        hash = hashlib.md5()
    elif algo == 'SHA1':
        hash = hashlib.sha1()
    elif algo == 'SHA256':
        hash = hashlib.sha256()
    with open(fname) as handle: #opening the file one line at a time for memory considerations
        for line in handle:
            hash.update(line.encode(encoding = 'utf-8'))
    return(hash.hexdigest())
layout = [
    [sg.Text('File 1'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('MD5'), sg.Checkbox('SHA1')
     ],
    [sg.Text('File 2'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('SHA256')
     ],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('File Compare', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        file1 = file2 = isitago = None
        # print(values[0],values[3])
        if values[0] and values[3]:
            file1 = re.findall('.+:\/.+\.+.', values[0])
            file2 = re.findall('.+:\/.+\.+.', values[3])
            isitago = 1
            if not file1 and file1 is not None:
                print('Error: File 1 path not valid.')
                isitago = 0
            elif not file2 and file2 is not None:
                print('Error: File 2 path not valid.')
                isitago = 0
            elif values[1] is not True and values[2] is not True and values[4] is not True:
                print('Error: Choose at least one type of Encryption Algorithm')
            elif isitago == 1:
                print('Info: Filepaths correctly defined.')
                algos = [] #algos to compare
                if values[1] == True: algos.append('MD5')
                if values[2] == True: algos.append('SHA1')
                if values[4] == True: algos.append('SHA256')
                filepaths = [] #files
                filepaths.append(values[0])
                filepaths.append(values[3])
                print('Info: File Comparison using:', algos)
                for algo in algos:
                    print(algo, ':')
                    print(filepaths[0], ':', hash(filepaths[0], algo))
                    print(filepaths[1], ':', hash(filepaths[1], algo))
                    if hash(filepaths[0],algo) == hash(filepaths[1],algo):
                        print('Files match for ', algo)
                    else:
                        print('Files do NOT match for ', algo)
        else:
            print('Please choose 2 files.')
window.close()

# ===============================================# 
он даст нам такой результат:

#image#

Заключительные мысли

Может это и не самый красивый пользовательский интерфейс, но PySimpleGUI позволяет вам быстро разворачивать простые пользовательские интерфейсы Python и делиться ими с кем угодно. Код, который вам нужен для этого, прост и легко читается. У вас все еще будет проблема запуска кода для получения пользовательского интерфейса. Из-за этого могут возникнуть сложности с совместным использованием кода. Советую скачать что-то вроде PyInstaller, который превратит ваш скрипт на python в .exe файл. Люди смогут запустить его просто нажав на него дважды.

