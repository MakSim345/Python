Python: вещи, которых вы могли не знать из песочницы

Python — красивый и местами загадочный язык. И даже зная его весьма неплохо, рано или поздно находишь для себя нечто такое, что раньше не использовал. Этот пост отражает некоторые детали языка, на которые многие не обращают внимание. Сразу скажу: многие примеры являются непрактичными, но, оттого, не менее интересными. Так же, многие примеры демонстрируют unpythonic стиль, но я и не претендую на новые стандарты — я просто хочу показать, что можно делать вот так.

1. Бесконечно вложенный список

>>> a = [1, 2, 3, 4]
>>> a.append(a)
>>> a
[1, 2, 3, 4, [...]]
>>> a[4]
[1, 2, 3, 4, [...]]
>>> a[4][4][4][4][4][4][4][4][4][4] == a
True


То же самое со словарями:

>>> a = {}
>>> b = {}
>>> a['b'] = b
>>> b['a'] = a
>>> print a
{'b': {'a': {...}}}



2. Форматирование списка

>>> l = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
>>> sum(l, [])
[1, 2, 3, 4, 5, 6, 7, 8, 9]


Генератором списков (спасибоmagic4x):

[y for x in data for y in x]


Альтернативные, но более длинные варианты (спасибо monolithed):

import itertools
data = [[1, 2, 3], [4, 5, 6]]
list(itertools.chain.from_iterable(data))


from functools import reduce
from operator import add
data = [[1, 2, 3], [4, 5, 6]]
reduce(add, data)



3. Генератор словарей

Многие знают про генератор списков, а как насчет генераторов словарей?

>>> {a:a**2 for a in range(1, 10)}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}



4. Одноразовая функция в классе

На тот случай, если вам нужна функция, которая будет использоваться всего один раз, после чего будет использоваться другая функция:

class foo:
    def normal_call(self):
        print("normal_call")
    def call(self):
        print("first_call")
        self.call = self.normal_call


>>> y = foo()
>>> y.call()
first_call
>>> y.call()
normal_call
>>> y.call()
normal_call



5. Получение аттрибутов класса

class GetAttr(object):
    def __getattribute__(self, name):
        f = lambda: "Hello {}".format(name)
        return f


>>> g = GetAttr()
>>> g.Mark()
'Hello Mark'



6. Операции над множествами

Set — множество, в котором отсутствуют повторяющиеся элементы:

>>> a = set([1,2,3,4])
>>> b = set([3,4,5,6])
>>> a | b # Объединение
{1, 2, 3, 4, 5, 6}
>>> a & b # Пересечение
{3, 4}
>>> a < b # Подмножества
False
>>> a - b # Разница
{1, 2}
>>> a ^ b # Симметрическая разность
{1, 2, 5, 6}


Без множества set эти операции работать не будут. Если только это не генератор множеств (спасибо ZyXI):

{ x for x in range(10)} # Генератор множеств

set([1, 2, 3]) == {1, 2, 3}
set((i*2 for i in range(10))) == {i*2 for i in range(10)}



7. Операторы сравнения

>>> x = 5
>>> 1 < x < 10
True
>>> 10 < x < 20 
False
>>> x < 10 < x*10 < 100
True
>>> 10 > x <= 9
True
>>> 5 == x > 4
True



8. Динамичное создание новых классов

>>> NewType = type("NewType", (object,), {"x": "hello"})
>>> n = NewType()
>>> n.x
'hello'


Этот же вариант в обычном виде:

>>> class NewType(object):
>>>     x = "hello"
>>> n = NewType()
>>> n.x
"hello"



9. Подавление исключения «KeyError» в словарях

В словарях существует метод .get(). В обычном случае, если вы вызываете несуществующий ключ name_dict['key'], вы получите исключение KeyError. Однако, если вызвать ключ через метод d.get('key'), то исключения не будет и, если ключа нет, то словарь возвратит None. Если вы хотите назначить переменную вместо отсутствующего ключа, то можно назначить второй параметр: d.get('key', 0).

Лучше всего это применять при переборе числовых ключей:

sum[value] = sum.get(value, 0) + 1



10. Добавление в список, находящийся в словаре

Если вам необходимо хранить несколько значений ключей, то вы можете хранить их в списке:

>>> d = {}
>>> a, b = 4, 5
>>> d[a] = list()
>>> d
{4: []}
>>> d[a].append(b)
>>> d
{4: [5]}



11. Назначение переменных по условию

x = 1 if (y == 10) else 2 # X равно 1, при условии, что Y равен 10. Если это не так - X равен 2
x = 3 if (y == 1) else 2 if (y == -1) else 1  # Более длинное условие. Не используйте здесь elif



12. Распаковка значений на переменные

Если при присваивании значений их окажется больше переменных — добавьте в начало имени переменной звездочку и ей будут присвоены остальные переменные (только Python 3.x):

>>> first,second,*rest = (1,2,3,4,5,6,7,8)
>>> first # Первое значение
1
>>> second # Второе значение
2
>>> rest # Все остальные значения
[3, 4, 5, 6, 7, 8]


>>> first,*rest,last = (1,2,3,4,5,6,7,8)
>>> first
1
>>> rest
[2, 3, 4, 5, 6, 7]
>>> last
8



13. Нумерация элементов списка

>>> l = ["spam", "ham", "eggs"]
>>> list(enumerate(l)) 
>>> [(0, "spam"), (1, "ham"), (2, "eggs")]
>>> list(enumerate(l, 1)) # Можно указать начало нумерации в качестве аргумента
>>> [(1, "spam"), (2, "ham"), (3, "eggs")]



14. Использование else в исключениях

Спасибо за исправление animeshneG

try: 
  function()
except Error:
  # Если не сработал try и объявлена ошибка Error
else:
  # Если сработал try и не сработал except
finally:
  # Выполняется в любом случае



15. Создание копии списка

При создании копии обычным методом произойдет следующее:

>>> x = [1, 2, 3]
>>> y = x
>>> y[2] = 5
>>> y
[1, 2, 5]
>>> x
[1, 2, 5]


Правильный вариант:

>>> x = [1,2,3]
>>> y = x[:]
>>> y.pop()
3
>>> y
[1, 2]
>>> x
[1, 2, 3]


Копирование вложенных списков & словарей (спасибо denisbalyko)

import copy
my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]} 
my_copy_dict = copy.deepcopy(my_dict)



16. Нумерация в for

Для нумерации элементов при выводе через цикл for используйте метод enumerate

>>> l = ['a', 'b', 'c', 'd', 'e']
>>> for i, value_list in enumerate(l, 1): # Аттрибут 1 - начало сортировки
>>>     print(i, value_list)
...     
1 a
2 b
3 c
4 d
5 e



17. Значения функции по умолчанию

При назначении функциям неправильные аргументы по умолчанию может получится нечто такое:

>>> def foo(x=[]):
...     x.append(1)
...     print x
... 
>>> foo()
[1]
>>> foo() 
[1, 1] # А должно быть [1]
>>> foo()
[1, 1, 1]



Вместо этого присваивайте аргументу значение None по умолчанию:

>>> def foo(x=None):
...     if x is None:
...         x = []
...     x.append(1)
...     print x
>>> foo()
[1]
>>> foo()
[1]



18. Метод __missing__ для словарей

Метод __missing__ позволяет избавить от исключения KeyError, возвращая вместо ошибки — имя запрошенного ключа.

class MyDict(dict): # Функция создания словаря
    def __missing__(self, key):
        return key
...
>>> m = MyDict(a=1, b=2, c=3) # Создание словаря через функцию
>>> m
{'a': 1, 'c': 3, 'b': 2}
>>> m['a'] # Ключ существует и вернет 1
1
>>> m['z'] # Ключа не существует и вернет имя запрошенног ключа
'z' 



19. Декораторы

Декораторы позволяют обернуть одну функцию другой, добавляя в нее функциональные возможности. Для обозначения декоратора на строку выше функции вы пишите знак "@"<имя функции>. 
Пример:

>>> def print_args(function):
>>>     def wrapper(*args, **kwargs):
>>>         print 'Аргументы функции: ', args, kwargs
>>>         return function(*args, **kwargs)
>>>     return wrapper

>>> @print_args
>>> def write(text):
>>>     print text
>>> write('foo')

Arguments: ('foo',) {}
foo


Объяснить попроще может только документация:

@f1(arg)
@f2
def func(): pass


эквивалентно коду

def func(): pass
func = f1(arg)(f2(func))



20. Обмен значениями между переменными

>>> a = 10
>>> b = 5
>>> a, b
(10, 5)
>>> a, b = b, a
>>> a, b
(5, 10)



21. Функции первого класса

>>> def jim(phrase):
...   return 'Jim says, "%s".' % phrase
>>> def say_something(person, phrase):
...   print person(phrase)

>>> say_something(jim, 'hey guys') # Передаем второй функции первую
'Jim says, "hey guys".'



Функции высшего порядка (спасибо Andrey_Solomatin):

# Здесь рассматривается функция высшего порядка g(), которая в качестве первого аргумента принимает функцию. 
# В результате на экран будет выведено  "100" (результат вычисления (7+3)×(7+3)).
def f(x):
    return x + 3
 
def g(function, x):
    return function(x) * function(x)
 
print g(f, 7)



22. Отрицательный round

>>> round(1234.5678, -2)
1200.0
>>> round(1234.5678, 2)
1234.57



23. Дзен Python

import this

24. Использование стиля C т.е. {} вместо отступов

Это, возможно, зло, но если вам хочется использовать скобки {} вместо отступов, для обозначения областей:

from __future__ import braces

25. Шаг в срезе списка

a = [1,2,3,4,5]
>>> a[::2]  # Указываем шаг
[1,3,5]


Значение -1 равносильно методу reverse — переворачивает список:

>>> a[::-1] # Переворачиваем список
[5,4,3,2,1]



26. Открытие вкладки в браузере

Открывает вкладку с указанным адресом в браузере по умолчанию.

import webbrowser
webbrowser.open_new_tab('http://habrahabr.ru/') # Вернет True и откроет вкладку



27. zip. Объединение списков

a = [(1,2), (3,4), (5,6)]
zip(*a)
# [(1, 3, 5), (2, 4, 6)]


Слияние двух списков в словарь:

>>> t1 = (1, 2, 3)
>>> t2 = (4, 5, 6)
>>> dict (zip(t1,t2))
{1: 4, 2: 5, 3: 6}



28. Срезы в списках и работа с ними

>>> a = range(10)
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a[:5] = [42] # Все символы до 5 заменяются элементом "42"
>>> a
[42, 5, 6, 7, 8, 9]
>>> a[:1] = range(5) 
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> del a[::2] # Удаление каждого второго элемента
>>> a
[1, 3, 5, 7, 9]
>>> a[::2] = a[::-2] # Альтернатива reserved
>>> a
[9, 3, 5, 7, 1]



29. Хранение нескольких элементов в ключе словаря

Если на ключ нужно назначить больше одного элемента, лучше хранить их в списке:

>>> m = {}
>>> m.setdefault('foo', []).append(1)
>>> m
{'foo': [1]}
>>> m.setdefault('foo', []).append(2)
>>> m
{'foo': [1, 2]}



30. Последнее и самое главное
Ради всего неизвестного, читайте ДОКУМЕНТАЦИЮ! Не собирайте очередной велосипед — возможно ваш код еще кому-то читать. Ни одна книга не сможет отразить полноту документации, а документация у Python отличная.

UPD:
31. Alex222 | комментарий

import antigravity



32. tanenn | комментарий
Использование else в цикле for:

>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print n, 'equals', x, '*', n/x
...             break
...     else:
...         # loop fell through without finding a factor
...         print n, 'is a prime number'



33. monolithed | комментарий
Пишем первую программу — "Hello World!"

import __hello__


34. AndersonDunai | комментарий
OrderedDict или сортировка словарей:

>>> # Не сортированный словарь
>>> d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
>>> # Словарь сортирован по ключ
>>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
>>> # Сортировка по значениям
>>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
>>> # Сортировка по длине названия ключа
>>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])



35. AndersonDunai | комментарий
Изменение класса объекта на лету изнутри класса через self.__class__ (подробнее)
Показательный пример (спасибо dmitriko):

class Worm:
    def creep(self):
    print("i am creeping")

class Butterfly:
    def fly(self):
    print("i am flying")

creature = Worm()
creature.creep()
creature.__class__ = Butterfly
creature.fly()



36. skovorodkin | комментарий
Подсчет количества элементов (в примере — количество букв в слове):

from collections import Counter
Counter('habrahabr')  # Counter({'a': 3, 'h': 2, 'r': 2, 'b': 2})



37. assert
Assert — это специальная конструкция, позволяющая проверять предположения о значениях произвольных данных в произвольном месте программы. Данная конструкция используется в целях тестирования/отладки кода, например Вы можете написать такую инструкцию:

assert x>y 


и если данная инструкция вернет false будет возбуждено исключение AssertationError. По сути, данная инструкция

assert <test>, <data>


это краткий эквивалент такой:

 if __debug__:
              if not <test>:
                  raise AssertationError, <data> 
