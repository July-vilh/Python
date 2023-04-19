## ---------------------------------------------- DICTIONARY ---------------------------------------------------

ХРАНИТ КОЛЛЕКЦИЮ ЭЛЕМЕНТОВ, ГДЕ КАЖДЫЙ ЭЛЕМЕНТ ИМЕЕТ УНИКАЛЬНЫЙ КЛЮЧ И СВЯЗАННОЕ С НИМ ЗНАЧЕНИЕ

> СОЗДАЕТСЯ ПРИ ПОМОЩИ:
1) ФИГУРНЫХ СКОБОК my_dict = {}
2) Через функцию dict: my_dict = dict()
3) Dictionary = {ключ1:значение1, ключ2:значение2}
4) Ключи в словаре могут быть только СТРОКАМИ, ЦЕЛЫМИ ЧИСЛАМИ или ЧИСЛАМИ С ПЛАВАЮЩЕЙ ТОЧКОЙ
5) Значения в словаре могут быть ЛЮБОГО ТИПА 

```
my_dict = {}
print(type(my_dict))
```
> RESULT: <class 'dict'>

```
my_dict = {
    'name': 'Anna',
    'last_name':'Karenina',
    'age': 35,
    'department': 'IT'
}
print(my_dict)
```
> RESULT: {'name': 'Anna', 'last_name': 'Karenina', 'age': 35, 'department': 'IT'}

----------------- ПОЛУЧИТЬ КОНКРЕТНОЕ ЗНАЧЕНИЕ КЛЮЧА СО ВСЕГО СЛОВАРЯ

```
my_dict = {
    'name': 'Anna',
    'last_name':'Karenina',
    'age': 35,
    'department': 'IT'
}
print(my_dict)
print(my_dict['name'])
```
> RESULT: Anna

```
my_dict = {
    'name': 'Anna',
    'last_name':'Karenina',
    'age': 35,
    'department': 'IT'
}
print(my_dict['last_name'])
```
> RESULT: Karenina

------------------------------------- ЗАМЕНИТЬ ЗНАЧЕНИЕ НОВЫМ ПО ОПРЕДЕЛЕННОМУ КЛЮЧУ

```
my_dict = {
    'name': 'Anna',
    'last_name':'Karenina',
    'age': 35,
    'department': 'IT'
}
print(my_dict['last_name'])
my_dict['last_name'] = 'You'
print(my_dict)
```
> RESULT: Karenina

{'name': 'Anna', 'last_name': 'You', 'age': 35, 'department': 'IT'}

```
my_dict = {
    'name': 'Anna',
    'last_name':'Karenina',
    'age': 35,
    'department': 'IT'
}
print(len(my_dict))
```
> RESULT: 4

----------------------------------- ДОБАВИТЬ ЕЩЕ КЛЮЧ: ЗНАЧЕНИЕ К СЛОВАРЮ 

```
my_dict = {
    'name': 'Anna',
    'last_name':'Karenina',
    'age': 35,
    'department': 'IT'
}
my_dict['salary'] = 5000
print(my_dict)
```
> RESULT: {'name': 'Anna', 'last_name': 'Karenina', 'age': 35, 'department': 'IT', 'salary': 5000}



__________________________________________________________________________________________________________________________

--------------------------------- МЕТОДЫ СЛОВАРЕЙ -------------------------------------------

1) .KEYS() ИСПОЛЬЗУЕТСЯ ДЛЯ ВЫВОДА ТОЛЬКО КЛЮЧЕЙ СЛОВАРЯ
2) .ITEMS() ИСПОЛЬЗУЕТСЯ ДЛЯ СОЗДАНИЯ КОРТЕЖЕЙ С КЛЮЧАМИ И ЗНАЧЕНИЯМИ
3) .GET() МЕТОД ДЛЯ ПОЛУЧЕНИЯ ЗНАЧЕНИЯ ПО КЛЮЧУ
4) .CLEAR() ОЧИСТИТЬ СЛОВАРЬ
5) .COPY() СКОПИРОВАТЬ ВЕСЬ СЛОВАРЬ 
6) LEN() ПОЛУЧИТЬ ДЛИНУ СЛОВАРЯ
7) TYPE() УЗНАТЬ ТИП СЛОВАРЯ
8) MIN() ПОЛУЧИТЬ КЛЮЧ С МИНИМАЛЬНЫМ ЗНАЧЕНИЕМ
9) MAX() ПОЛУЧИТЬ КЛЮЧ С МАКСИМАЛЬНЫМ ЗНАЧЕНИЕМ
