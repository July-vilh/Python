### 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

```
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])
```
> RESULT: [1, 2, 3]

### 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

- получите сумму всех чисел
 
- распечатайте все строки, где есть буква 'a'
```
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
result = ([item for item in list_1 if isinstance(item, (int, float))])
print(sum(result))
```
> RESULT: 213
```
result_a = ([item for item in list_1 if isinstance(item, str) and 'a' in item])
print(result_a)
```
> RESULT: ['ananas', 'pizza']

### 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
```
list = ['cat', 'dog', 'horse', 'cow']
print(tuple(list))
```
> RESULT: ('cat', 'dog', 'horse', 'cow')

### 3.4. Напишите программу, которая определяет, какая семья больше.

1) Программа имеет два input() - например, family_1, family_2

2) Членов семьи нужно перечислить через запятую

Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

```
family_1 = tuple(input('Перечислите членов семьи через запятую: ').split(','))
family_2 = tuple(input('Перечислите членов семьи через запятую: ').split(','))
if len(family_1) == len(family_2):
    print('Equal')
elif len(family_1) > len(family_2):
    print('family_1')
else:
    print('family_2')
```
> RESULT: 

>Перечислите членов семьи через запятую: eri, sirius, july

>Перечислите членов семьи через запятую: eri, sirius

>family_1

### 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию о вашем любимом фильме.
 - распечатайте только ключи
 
 - распечатайте только значения
 
 - распечатайте пары ключ - значение
```
film = {
    'title': 'Вечное сияние чистого разума',
    'director': 'Мишель Гондри',
    'year': 2004,
    'budget': '20 млн долл',
    'slogan': '«Можно стереть любовь из памяти. Выкинуть из сердца — это уже другая история»'
}

print(film.keys())
print(film.values())
print(film)
```
>RESULT:
>dict_keys(['title', 'director', 'year', 'budget', 'slogan'])
>dict_values(['Вечное сияние чистого разума', 'Мишель Гондри', 2004, '20 млн долл', '«Можно стереть любовь из памяти. Выкинуть из сердца — это уже другая история»'])
>{'title': 'Вечное сияние чистого разума', 'director': 'Мишель Гондри', 'year': 2004, 'budget': '20 млн долл', 'slogan': '«Можно стереть любовь из памяти. Выкинуть из сердца — это уже другая история»'}

### 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
```
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))
```
> RESULT: 926

### 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
```
list = [1, 2, 3, 4, 5, 3, 2, 1]
delete = set(list)
print(delete)
```
>RESULT: {1, 2, 3, 4, 5}







