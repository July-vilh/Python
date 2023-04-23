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

Перечислите членов семьи через запятую: eri, sirius, july

Перечислите членов семьи через запятую: eri, sirius

family_1







