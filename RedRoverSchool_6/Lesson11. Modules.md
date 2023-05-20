1 --------------------------------------- МОДУЛЬ datetime (импорт + использование) ------------------------------------------

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
