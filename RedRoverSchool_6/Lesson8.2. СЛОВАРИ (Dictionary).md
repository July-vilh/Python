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

```
dct = dict(USA=1, Russia=7, Turkey=90)
print(dct)
```
> RESULT: {'USA': 1, 'Russia': 7, 'Turkey': 90}

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

------------------------------------- ЦИКЛ:
```
dct = {
    'USA' : '1',
    'Russia': '7',
    'Turkey': '90'
}

if 'USA' in dct:
    print('YES')
else:
    print('NO')
```
> RESULT: YES (тк ключ USA есть в данном словаре)
> 
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

----------------------------------------------------- МЕТОДЫ СЛОВАРЕЙ -------------------------------------------

1) .KEYS() ИСПОЛЬЗУЕТСЯ ДЛЯ ВЫВОДА ТОЛЬКО КЛЮЧЕЙ СЛОВАРЯ

```
my_dict = {
    'name': 'Anna',
    'last_name':'Karenina',
    'age': 35,
    'department': 'IT'
}
print(my_dict.keys())
```
> RESULT: dict_keys(['name', 'last_name', 'age', 'department'])

```
dct = {
    'USA' : '1',
    'Russia': '7',
    'Turkey': '90'
}
for key in dct.keys:
    print(key)
```
> RESULT: 
> 
> USA
> 
> Russia
> 
> Turkey

```
dct = {
    'USA' : '1',
    'Russia': '7',
    'Turkey': '90'
}
print(*dct, sep='\n')
```
> RESULT:
>  
> USA
> 
> Russia
> 
> Turkey

1.2) ВЫВОД ЗНАЧЕНИЙ:

```
my_dict = {
    'name': 'Anna',
    'last_name':'Karenina',
    'age': 35,
    'department': 'IT'
}

print(my_dict.values())
```
> RESULT: dict_values(['Anna', 'Karenina', 35, 'IT'])

```
dct = {
    'USA' : '1',
    'Russia': '7',
    'Turkey': '90'
}
for value in dct.values():
    print(value)
```
> RESULT: 
> 
> 1
> 
> 7
> 
> 90

---------------------------------- ВЫВОД СРАЗУ И КЛЮЧЕЙ И ЗНАЧЕНИЙ (ЦИКЛ):

```
dct = {
    'USA' : '1',
    'Russia': '7',
    'Turkey': '90'
}

for key, value in dct.items():
    print(key, value)
```
> RESULT: 
> 
> USA 1
> 
> Russia 7
> 
> Turkey 90


3) .ITEMS() ИСПОЛЬЗУЕТСЯ ДЛЯ СОЗДАНИЯ КОРТЕЖЕЙ С КЛЮЧАМИ И ЗНАЧЕНИЯМИ

```
my_dict = {
    'name': 'Anna',
    'last_name':'Karenina',
    'age': 35,
    'department': 'IT'
}

print(my_dict.items())
```
> RESULT: dict_items([('name', 'Anna'), ('last_name', 'Karenina'), ('age', 35), ('department', 'IT')])

5) .GET() МЕТОД ДЛЯ ПОЛУЧЕНИЯ ЗНАЧЕНИЯ ПО КЛЮЧУ

```
dct = {
    'USA' : '1',
    'Russia': '7',
    'Turkey': '90'
}

print(dct.get('USA'))
```
> RESULT: 1

-- ЕСли введенного ключа в словаре НЕТ то результатом будет None:

```
dct = {
    'USA' : '1',
    'Russia': '7',
    'Turkey': '90'
}

print(dct.get('France'))
```
> RESULT: None 

--- Типо ЗАМена None при ОТСУТСТВИИ страны:

```
dct = {
    'USA' : '1',
    'Russia': '7',
    'Turkey': '90'
}

print(dct.get('France', 'Нет такой страны'))
```
> RESULT: Нет такой страны

---------------- МЕтод setdefault = похож на Get но отличается тем, что можно добавить значение которого нет в словарь!!!!!

```
dct = {
    'USA' : '1',
    'Russia': '7',
    'Turkey': '90'
}

print(dct.setdefault('France'))
print(dct)
```
> RESULT:
> 
> None
> 
> {'USA': '1', 'Russia': '7', 'Turkey': '90', 'France': None}


```
dct = {
    'USA' : '1',
    'Russia': '7',
    'Turkey': '90'
}

print(dct.setdefault('France', '+75'))
print(dct)
```
> RESULT: +75
> 
> {'USA': '1', 'Russia': '7', 'Turkey': '90', 'France': '+75'}


7) .CLEAR() ОЧИСТИТЬ СЛОВАРЬ
8) .COPY() СКОПИРОВАТЬ ВЕСЬ СЛОВАРЬ 
9) LEN() ПОЛУЧИТЬ ДЛИНУ СЛОВАРЯ
10) TYPE() УЗНАТЬ ТИП СЛОВАРЯ
11) MIN() ПОЛУЧИТЬ КЛЮЧ С МИНИМАЛЬНЫМ ЗНАЧЕНИЕМ
12) MAX() ПОЛУЧИТЬ КЛЮЧ С МАКСИМАЛЬНЫМ ЗНАЧЕНИЕМ

12) МЕТОД pop СНАЧАЛА ВОЗВРАЩАЕТ ЗНАЧЕНИЕ КЛЮЧА ПОТОМ В ПРИНЦИПЕ УДАЛЯЕТ ВЕСЬ КЛЮЧ:

```
my_dict = {
    'name': 'Anna',
    'last_name':'Karenina',
    'age': 35,
    'department': 'IT'
}

print(my_dict.pop('department'))
print(my_dict)
```
> RESULT: IT

{'name': 'Anna', 'last_name': 'Karenina', 'age': 35}

13) МЕТОД get:

```
my_dict = {
    'name': 'Anna',
    'last_name':'Karenina',
    'age': 35,
    'department': 'IT'
}

print(my_dict.pop('department'))
print(my_dict)
print(my_dict.get('department'))
```
> RESULT: IT

{'name': 'Anna', 'last_name': 'Karenina', 'age': 35}


-_____________________________________________________________________________________

---------------------------- СОЗДАТЬ СЛОВАТЬ КОГДА ЕСТЬ КЛЮЧ И ЗНАЧЕНИЯ ОТДЕЛЬНО --------------------------------------

```
keys = ['name', 'last_name', 'department']
values = ['Anna', 'Karenina', 35]
employee = dict(zip(keys, values))
print(employee)
```
> RESULT: {'name': 'Anna', 'last_name': 'Karenina', 'department': 35}

```
employee1 = dict(name='Anna', last_name='Karenina', age=25)
print(employee1)
```
> RESULT: {'name': 'Anna', 'last_name': 'Karenina', 'age': 25}


------------------------------------------------- СЛИЯНИЕ СЛОВАРЕЙ --------------------------------------------

```
dct = {
    'USA' : '1',
    'Russia': '7',
    'Turkey': '90'
}

dct2 = {
    'name':'Anna',
    'last_name':'Karenina',
    'age': 45
}

dct3 = dct | dct2
print(dct3)
```
> RESULT: {'USA': '1', 'Russia': '7', 'Turkey': '90', 'name': 'Anna', 'last_name': 'Karenina', 'age': 45}
