1 --------------------------------------- МОДУЛЬ datetime (импорт + использование) ------------------------------------------

Представляет собой отдельный файл с кодом (т.е. я например отдельно создаю питоновский файл "module" в который помещаю функции например) который можно повторно использовать в других программах

Каждая программа может импортировать модуль и получить доступ к его классам, функциям, объектам

```
import module
print(module.sum(4, 5))
```
> RESULT: 9

Модули позволяют разбить ОГРОМНЫЕ программы на НЕБОЛЬШИЕ кусочки кода, которыми легко управлять и организовывать 

- import time
- import random as rand
- from math import sin, cos

Отображает сегодняшнюю дату 

РАССЧИТАТЬ ДР (datetime)

```
import datetime
bday = 1980
current_date = datetime.date.today()
age = current_date.year - bday
print(age)
```
> RESULT: 43


2 ------------------------------------- МОДУЛЬ math ------------------------------------------------


```
l1 = [20, 15, 8, 7, 6]
import math as m
print(m.prod(l1))
```
> RESULT: 100800 (т.к. 20*15*8*7*5 ВМЕСТО ЛЯМБДЫ ФУНКЦИИ)


------- СОЗДАТЬ ФАЙЛ module.py и В НЕГО ВНЕСТИ ФУНКЦИИ, НАПРИМЕР:

```
def hello(name):
    return f'Hello, {name}'

def sum(a, b):
    return a + b
```

В ОТДЕЛЬНОМ ФАЙЛЕ ПЕРЕДАВАТЬ ВЫВОД РЕЗУЛЬТАТА ЭТИХ ФУНКЦИЙ ПОСЛЕ ИМПОРТА

```
from module import hello, sum
print(hello('Sam'))
print(sum(5, 8))
```

> RESULT: Hello, Sam
> 13


----------------------- ПРОСТРАНСТВО ИМЕН ---------------------------------------

ПРОСТРАНСТОВ ИМЕН - это место, где хранится переменная. Пространства имен реализованы в виде СЛОВАРЕЙ, где КЛЮЧИ - это ИМЕНА ОБЪЕКТОВ, а ЗНАЧЕНИЯ = САМИ ОБЪЕКТЫ

1. ВСТРОЕНООЕ ПРОСТРАНСТВО ИМЕН (Built-in) содержит имена всех встроенных объектов (Python)
```
print(dir(__builtins__))
```
> RESYLT: ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning']


2. ГЛОБАЛЬНЫЕ (GLOBAL) ПРОСТРАНСТВА ИМЕН содержат имена на уровне основной программы, поэтому переменные, находящиеся в нем являются ГЛОБАЛЬНЫМИ. Глобальными могут быть импорты, например список со значениями 

```
print(globals())
```
> RESULT: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001FA8C464DD0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\Professional\\Desktop\\RedRoverSchool\\functions.py', '__cached__': None, 'l1': [20, 15, 8, 7, 6]}
print(f'locals: {locals()}')

3. ЗАМКНУТОЕ (ENCLOSED = когда одна функция находится внутри ДРУГОЙ) ПРОСТРАНСТВО ИМЕН включает имена определенные внутри внешней функции. Что-то вроде ДЕКОРАТОРОВ например

```
var = 'global'
def func1():
    def local():
        print(var)
    local()
func1()
```
> RESULT: global

Для изменения названия первоначальнозаданной переменной
```
var = 'global'
def func1():
    var = 'enclosed'
    def local():
        print(var)
    local()
func1()
```
> RESULT: enclosed

----------------- ПОИСК ИДЕТ ИЗНУТРИ НАРУЖУ:

```
var = 'global'
def func1():
    var = 'enclosed'
    def local():
        var = 'local'
        print(var)
    local()
func1()
print(f'outside: {var}')
```
> RESULT: local
> outside: global


5. ЛОКАЛЬНОЕ (LOCAL) ПРОСТРАНСТВО ИМЕН включает в себя локальные имена внутри функции.Переменные, которые находятся внутри функций называются ЛОКАЛЬНЫМИ

```
print(f'locals: {locals()}')
```
> RESULT: locals: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001FA8C464DD0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\Professional\\Desktop\\RedRoverSchool\\functions.py', '__cached__': None, 'l1': [20, 15, 8, 7, 6]}

Локальными переменными мб переменные которые присвоены какой-нибудь функции например 


--------------------------------------------------------------- ОБЛАСТЬ ВИДИМОСТИ (SCOPE) ---------------------------------------------------------------------

Это ПРАВИЛО поиска привязок (значение с назначенным именем), а ПРОСТРАНСТОВ ИМЕН это СЛОВАРЬ для хранения всех переменных

ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ = переменные которые не определены внутри какой-то функции + они видны ВО ВСЕМ участке кода

ПРИМЕР ГЛОБАЛЬНЫХ ПЕРЕМЕННЫХ:

```
age = 17

def print_age():
    print(age)

print_age()
```
> RESULT: 17

ЛОКАЛЬНЫЕ = это те которые внутри интерфейса и их область видимости ограниена только внутри самой функции

ПРИМЕР ЛОКАЛЬНЫХ ПЕРЕМЕННЫХ:

```
def print_age():
    age = 17
    print(age)
print_age()
```
>RESULT: 17

```
def fun():
    print(f'First {s}')
s = 'Hello'
fun()
print(f'Second {s}')
```
> RESULT: 
> First Hello
> Second Hello

```
def fun():
    s = 'Hi'
    print(f'First {s}')
s = 'Hello'
fun()
print(f'Second {s}')
```
> RESULT: 
> First Hi
> Second Hello

- ОБЪЕМЛЮЩЕЕ ПРОСТРАНСТВО ИМЕН = когда одна функция определена ВНУТРИ другой функции. ВНУТРЕННЯЯ ФУНКЦИЯ также известна как вложенная и может обращаться к переменным определенным во ВНЕШНЕЙ ФУНКЦИИ

ПРИМЕР ОБЪЕМЛЮЩЕГО ПРОСТРАНСТВА:

```
def multi():
    x = 10
    y = 5

    def sum_fun():
        c = 20
        print(x + y + c)
    sum_fun()
multi()
```
> RESULT: 35

```
def multi():
    x = 10
    print(x + y + c)
    def sum_fun():
        c = 20
    sum_fun()
y = 5
multi()
``` 
> RESULT: НО ТУТ БУДЕТ ОШИБКА, тк ГЛУБЖЕ ПЕРЕМЕННУЮ (с) ОНО УЖЕ НЕ ВИДИТ, только из ГЛУБИНЫ ВО ВНЕШНЕЕ 

```
def multi():
    x = 10
    print(x + y + c)
    def sum_fun():
        c = 20
        print(x + y + c)
    sum_fun()
y = 5
c = 30
multi()
```
> RESULT: 45
> 35



