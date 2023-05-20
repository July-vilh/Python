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
