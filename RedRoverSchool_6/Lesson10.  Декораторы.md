------------------------------- ДЕКОРАТОРЫ -------------------------------

Представляют функцию, которая в качестве параметра получает функцию и в качестве результата также возвращает функцию. Декораторы позволяют модифицировать выполняемую функцию.

Т.е декоратор ПОЗВОЛЯЕТ ОБЕРНУТЬ ДРУГУЮ ФУНКЦИЮ для расширения ее функциональности БЕЗ НЕПОСРЕДСТВЕННОГО ИЗМЕНЕНИЯ ЕЕ КОДА 

```
def decorator_function(func):
    def wrapper():
        print('Функция-обертка!')
        print(f'ОБОРАЧИВАЕМАЯ ФУНКЦИЯ: {func}')
        print('ВЫПОЛНЯЕМ ОБЕРНУТУЮ ФУНКЦИЮ...')
        func()
        print('ВЫХОДИМ ИЗ ОБЕРТКИ')
    return wrapper
```


_________________________________________________

```
def my_decorator(func):
    def wrapper():
        print('Я-обертка!')
        func()
        print('Завернули')
    return wrapper()

def say_hello():
    print(f'Hello')

say_hello = my_decorator(say_hello)
```

> RESULT: 
> Я-обертка!
> Hello
> Завернули


_________________________________________________________

```
def my_decorator(func):
    def wrapper():
        print('Я-обертка!')
        func()
        print('Завернули')
    return wrapper()

@my_decorator
def say_hello():
    print(f'Hello')
```

АНАЛОГ КОДА ДЛЯ СТРОКИ say_hello = my_decorator(say_hello) (= @my_decorator)

> RESULT: 
> Я-обертка!
> Hello
> Завернули


--------------------------------- Если нам нужно передать еще доп. параметр в функции например {name}, то к wrapper и func ДОБАВЛЯЕМ (arg) + у return wrapper удаляем скобки и 

------------- + вызываем функцию со стакой которую хотим передать say_hello('Sam"):


```
def my_decorator(func):
    def wrapper(arg):
        print('Я-обертка!')
        func(arg)
        print('Завернули')
    return wrapper

@my_decorator
def say_hello(name):
    print(f'Hello,{name}')

say_hello(' Sam')
```
> RESULT: 
> Я-обертка!
> Hello, Sam
> Завернули


___________________________________________________________________________________________

```
def milk(func):
    def wrapper():
        print('hot milk')
        func()
    return wrapper()


def sugar(func):
    def wrapper():
        print('sugar')
        func()
    return wrapper()

@milk
def coffee():
    print('Coffee')
```

> RESULT:
> hot milk
> Coffee


_________________________________________________
РАССЧИТАТЬ ДР (datetime)

```
import datetime
bday = 1980
current_date = datetime.date.today()
age = current_date.year - bday
print(age)
```
> RESULT: 43

