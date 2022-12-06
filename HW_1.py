# 1) Создать переменную типа String
item ='July'
print(item)
print(type(item))

# 2) Создать переменную типа Integer
item2 = 0
print(item2)
print(type(item2))

# 3) Создать переменную типа Float
item3 = 2.5
print(item3)
print(type(item3))

# 4) Создать переменную типа Bytes
item4=bytes('Строка байт', encoding = 'utf-8')
print(item4)
print(type(item4))

# 5) Создать переменную типа List
item5 = [True, 786, 3.14, 'text', 70.2]
print(item5)
print(type(item5))

# 6) Создать переменную типа Tuple (кортеж)
item6 = [5], [1, 2, 3, 4]
print(item6)
print(type(item6))

# 7) Создать переменную типа Set
item7 = {"hi", "bye"}
print(item7)
print(type(item7))

# 8) Создать переменную типа Frozenset (неизменяемое множество)
ls1 = [0, 1, 2, 3, 4]
item8 = frozenset(ls1)
print(item8)
print(type(item8))

# 9) Создать переменную типа Dict
item9 = {'dict': 1, 'dictionary': 2}
print(item9)
print(type(item9))

# 10) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
a = 'July'
b = 'Vlad'
c = a + b
print(c)

# 11) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
a = 'July, '
b = 25
c = a + str(b)
print(c)

# 12) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
a = 'July+'
b = 25
c = a + str(b)
print(c)
