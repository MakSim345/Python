Отслеживаем прогресс выполнения в Python
10 января 2020.
("https://habr.com/ru/post/483400/")

Зачем нужны индикаторы прогресса?

Индикаторы прогресса (progress bar) — визуальное отображение процесса работы. Они избавляют нас от необходимости беспокоиться о том, не завис ли скрипт, дают интуитивное представление о скорости его выполнения и подсказывают, сколько времени осталось до завершения.


Человек ранее не использовавший индикаторы прогресса может предположить, что их внедрение может сильно усложнить код. К счастью, это не так. Небольшие примеры ниже покажут, как быстро и просто начать отслеживать прогресс в консоли или в интерфейсе быстро набирающей популярность графической библиотеки PySimpleGUI.


=========================================================
Используем Progress

Первым у нас идёт модуль "Progress" ("https://github.com/verigak/progress/")


Всё, что от вас потребуется, это указать количество ожидаемых итераций, тип индикатора и вызывать функцию при каждой итерации:


import time
from progress.bar import IncrementalBar

mylist = [1,2,3,4,5,6,7,8]

bar = IncrementalBar('Countdown', max = len(mylist))

for item in mylist:
    bar.next()
    time.sleep(1)

bar.finish()

=========================================================
Используем "tqdm" 
Следующей на очереди идёт библиотека "tqdm" ("https://github.com/tqdm/tqdm")
Быстрый и расширяемый индикатор прогресса для Python и CLI

Всего один вызов функции понадобится для получения результата аналогичного предыдущему:

import time
from tqdm import tqdm

mylist = [1,2,3,4,5,6,7,8]

for i in tqdm(mylist):
    time.sleep(1)

Само собой, в комплекте идёт куча настроек и опций.

=========================================================
Используем "alive-progress" ("https://github.com/rsalmei/alive-progress")

Ещё один вариант синтаксиса, побольше дефолтных анимаций, чем в предыдущих примерах:


from alive_progress import alive_bar
import time

mylist = [1,2,3,4,5,6,7,8]

with alive_bar(len(mylist)) as bar:
    for i in mylist:
        bar()
        time.sleep(1)


=========================================================
GUI индикатор прогресса для скрипта

Иногда возникает необходимость предоставить конечному пользователю графический индикатор.
Сколько кода нужно, чтобы достигнуть такого результата? Немного:

import PySimpleGUI as sg
import time

mylist = [1,2,3,4,5,6,7,8]

for i, item in enumerate(mylist):
    sg.one_line_progress_meter('This is my progress meter!', i+1, len(mylist), '-key-')
    time.sleep(1)

Индикатор в приложении "PySimpleGUI" ("https://github.com/PySimpleGUI/PySimpleGUI")

Рассмотрим реализацию индикатора в PySimpleGUI.

Вот как это сделать:


import PySimpleGUI as sg
import time

mylist = [1,2,3,4,5,6,7,8]

progressbar = [
    [sg.ProgressBar(len(mylist), orientation='h', size=(51, 10), key='progressbar')]
]
outputwin = [
    [sg.Output(size=(78,20))]
]

layout = [
    [sg.Frame('Progress',layout= progressbar)],
    [sg.Frame('Output', layout = outputwin)],
    [sg.Submit('Start'),sg.Cancel()]
]

window = sg.Window('Custom Progress Meter', layout)
progress_bar = window['progressbar']

while True:
    event, values = window.read(timeout=10)
    if event == 'Cancel'  or event is None:
        break
    elif event == 'Start':
        for i,item in enumerate(mylist):
            print(item)
            time.sleep(1)
            progress_bar.UpdateBar(i + 1)

window.close()

Заключение

Как видите, нет ничего сложного в добавлении информации о прогрессе выполнения: кода немного, а отзывчивость повышается очень сильно. Используйте индикаторы, чтобы больше никогда не гадать, завис ли процесс или нет!

