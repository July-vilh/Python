# Список чисел

l1 = [1, 2, 3, 4, 5]
print(l1)

# РЕЗУЛЬТАТ: 
[1, 2, 3, 4, 5]

____________________________________________

# Список состоящий из типа данных string

names = ['Anna', 'Alex', 'Victor']
print(names)

# РЕЗУЛЬТАТ:
['Anna', 'Alex', 'Victor']
_________________________________________

print(type(l1))
print(type(names))

# РЕЗУЛЬТАТ:
<class 'list'>
<class 'list'>
__________________________________________

# Пустые списки
l1 = []
l2 = list()

#Список с разными типами данных
l3 = [9, 3.14, 'Text', True, False, [1,6,3], {'name':'Anna'}]

____________________________________________

# Разбиение строки целостной на ОТДЕЛЬНЫЕ ЭЛЕМЕНТЫ!
item1 = 'Yolochka'
l4 = list(item1)
print(l4)

# РЕЗУЛЬТАТ:
['Y', 'o', 'l', 'o', 'c', 'h', 'k', 'a']

______________________________________________________
# Вывод например второго элемента строки (1):
print(item1[1])

# РЕЗУЛЬТАТ: о

#Вывод первого элемента строки (0):
print(item1[0])

# РЕЗУЛЬТАТ: Y
________________________________________________________________
# Умножение элементов (ИХ КОЛИЧЕСТВА, НЕ САМИ ЗНАЧЕНИЯ) внутри списка:

l5 = [3]
l55 = l5 * 4
print(l55)

# РЕЗУЛЬТАТ:
[3, 3, 3, 3]

___________________________________________________________________

#Умножение значения string:
l6 = ['Anna']
l66 = l6 * 4
print(l66)

# РЕЗУЛЬТАТ:
['Anna', 'Anna', 'Anna', 'Anna']
