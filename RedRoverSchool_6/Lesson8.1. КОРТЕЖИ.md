## ------------------------------------------- КОРТЕЖИ TUPLES ------------------------------------

> Создаются при помощи КРУГЛЫХ СКОБОК () либо с помощью ФУНКЦИИ TUPLE() ИЛИ ПРИ ПЕРЕЧИСЛЕНИИ ЗНАЧЕНИЙ ЧЕРЕЗ ЗАПЯТУЮ

1) MY_TUPLE = ()
```
MY_TUPLE = (1, 2, 3, 4)
print(MY_TUPLE)
```
> RESULT: (1, 2, 3, 4)

2) MY_TUPLE = TUPLE()
```
MY_TUPLE = tuple('Mark')
print(MY_TUPLE)
```
> RESULT: ('M', 'a', 'r', 'k')

3) MY_TUPLE = 1, 2, 3, 4
```
MY_TUPLE = 1, 2, 3, 4
print(MY_TUPLE)
```
> RESULT: (1, 2, 3, 4)

4) 
```
name = 'Mark',
print(name)
```
> RESULT: ('Mark',)

__________________
> ЭЛЕМЕНТЫ ВНУТРИ КОРЕЖЕЙ РАЗДЕЛЯЮТСЯ ЗАПЯТЫМИ
> ТЮПЛЫ МОГУТ ХРАНИТЬ РАЗНЫЕ ТИПЫ ДАННЫХ 
> ПРИМЕНЯЮТСЯ КОГДА НУЖНО СОХРАНИТЬ ЦЕЛОСТНОСТЬ ДАННЫХ 
> С ПОМОЩЬЮ КОРТЕЖЕЙ МОЖНО ПЕРЕДАВАТЬ В ФУНКЦИЮ ПРОИЗВОЛЬНОЕ КОЛИЧЕСТВО АРГУМЕНТОВ 

```
def func (*args):
    for item in args:
        return item*item
print(func(2,5,6,8,10))
``` 
> RESULT: 4 + СИМВОЛ * ОЗНАЧАЕТ ЧТО ТЮПЛ НАДО РАСПАКОВАТЬ!

```
def sum_it(*args):
    total = 0
    for num in args:
        total = total + num
    return(total)
print(sum_it(4, 5, 10, 6, 20))
```

> RESULT: 45
_________________________________________________________________________________

### ------------------- ДЕКОМПОЗИЦИЯ ТЮПЛА (Т.Е. КАЖДЫЙ ЭЛЕМЕНТ ТЮПЛА СОХРАНИТЬ В ОТДЕЛЬНУЮ ПЕРЕМЕННУЮ) ----------------

``` 
my_tuple = ('apple', 'banana', 'cat')
a, b, c = my_tuple
print(a)
print(b)
print(c)
``` 

> RESULT: 
 
apple

banana

cat

__________________________________________

!!!!!!!!!!!!!!!!!!!ЧТО БЫ КАКАИЕ-ТО ЭЛЕМЕНТЫ (НАПРИМЕР ПЕРВЫЙ ЭЛЕМЕНТ) ТЮПЛА ЗАМЕНИТЬ ДРУГОЙ ПЕРЕМЕННОЙ ДЛЯ ЭТОГО НУЖНО ПРЕОБРАЗОВАТЬ ТЮПЛ В ЛИСТ!!!!!!!!!!!!

``` 
my_tuple = ('apple', 'banana', 'cat')
letters = list(my_tuple)
letters[0] = 'ananas'
print(letters)
``` 

> RESULT: ['ananas', 'banana', 'cat']

``` 
my_tuple = (1, 'name', None, 'name', 'name', 25)
print(my_tuple.index('name'))
print(my_tuple.count('name'))
``` 
> RESULT: 1 3

### ЕСЛИ НАДЮ ВЫВЕСТИ ТОЛЬКО ЦИФРЫ ИЗ ТЮПЛА 

``` 
my_tuple = (1, 'name', None, 'name', 'name', 25)
result = tuple([item for item in my_tuple if isinstance(item, int)])
print(result)
``` 
> RESULT: (1, 25)

> верни элемент для кажого элемента в тюпле если * [isinstance = МЕТОД, КОТОРЫЙ ПРОВЕРЯЕТ ТИП ДАННЫХ В ТЮПЛЕ] будет целым числом 

                               ------------------------------- МЕТОДЫ ТЮПЛОВ -----------------------

```
my_tuple = (1, 'name', None, 'name', 'name', 25)
result = tuple([item for item in my_tuple if isinstance(item, int)])
print(result)

print(f'Sum is: {sum(result)}')
print(f'Max is: {max(result)}')
print(f'Min is: {min(result)}')
print(f'Length of my tuple is: {len(my_tuple)}')
print(f'Length of the result is: {len(result)}')
```

> RESULT: 

(1, 25)

Sum is: 26

Max is: 25

Min is: 1

Length of my tuple is: 6

Length of the result is: 2

------------------------------------------ ЦИКЛ В ТЮПЛЕ (ЦИКЛ FOR) ----------------------------------------------------

Для того что бы пройтись по ТЮПЛУ и после чего отобразить его индекс

```
for (index, item) in enumerate(my_tuple):
    print(index, item)
```
> RESULT:

0 1

1 name

2 None

3 name

4 name

5 25

---------------------------------------- ЦИКЛ В ТЮПЛЕ (ЦИКЛ WHILE) -----------------------------------------

```
i = 0
while i < len(my_tuple):
    print(i, my_tuple[i])
    i+=1
```

> RESULT:

0 1

1 name

2 None

3 name

4 name

5 25

-------------------------------------------- ВЛОЖЕННЫЕ СПИСКИ В ТЮПЛЫ --------------------------------------------

```
fruits = ('apple', ['ananas', 'mango'], 'melon')
fruits[1][0] = 'cherry'
print(fruits)
```

> RESULT: ('apple', ['cherry', 'mango'], 'melon')

ТУТ ПРОИСХОДИТ ЗАМЕНА НУЛЕВОГО ЭЛЕМЕНТА ПЕРВОГО ИНДЕКСА В ТЮПЛЕ НА НОВОЕ ЗНАЧЕНИЕ

------------------------------------- ПОМЕНЯТЬ ПЕРЕМЕННЫЕ МЕСТАМИ (ЧТО БЫ СТАЛО НАОБОРОТ) --------------------------------

```
a = 5
b = 10
a, b = b, a
print(f'a= {a}')
print(f'b = {b}')
```

> RESULT: 

a= 10

b = 5

ЧЕРЕЗ ТЕКНИХУ a, b = b, a

------------------------------- 

--------------------------------------------------- ДЛЯ ПОДСЧЕТА ПЕРЕДАННЫХ ЗГАЧЕНИЙ -------------------------------------------------------
```
def sum_it(*args):
    total = 0
    for num in args:
        total = total + num
    return(total)
print(sum_it(4, 5, 10, 6, 20))
print(sum_it(4, 5, 10, 6, 20, 4, 5, 10, 6, 20))
```

> RESULT: 45
          90
          
 ``` 
 def func(*args):
    l = []
    print(len(args))
    for item in args:
        l.append(item*item)
    return l
print(func(2, 5, 6, 8, 10))
```

> RESULT: 5

[4, 25, 36, 64, 100]

