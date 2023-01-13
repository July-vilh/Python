#2. Добавить слово в конец списка так, чтобы каждая буква стала отдельным элементом списка

l = [1, 2, 3]
a = 'abc'
# result = [1, 2, 3, 'a', 'b', 'c']

# extend() добавляет новые элементы (несколько) в конец списка (все а добавляем в l):
l.extend(a)
print(l)

# append добавляет только 1 аргумент (в отличии от extend) + решение через цикл (1 элемент i который является а добавляем в l):
for i in a:
    l.append(i)
print (l)

# еще одно решение:
l += a
print (l)
____________________________

# 3. Все чётные числа вывести в другой список
l = [1,3,4,5,8,9,10,44,22,50,79,54,28,91]
# Оператор ОСТАТОК ОТ ДЕЛЕНИЯ = %

k = []
for i in l:
    if i % 2 == 0:
        k.append(i)
print(k)
print(l)

# РЕЗУЛЬТАТ: [4, 8, 10, 44, 22, 50, 54, 28]
#            [1, 3, 4, 5, 8, 9, 10, 44, 22, 50, 79, 54, 28, 91]

_______________________________

# 4. Все emails у которых есть слово test вывести в другой список
l = ['webtest1@gmail.com',
     'alex_dr5@gmail.com',
     'elena_viktorovna@gmail.com',
     'infotest@gmail.com',
     'sigmatesst@gmail.com',
     'planet.dollsatest@gmail.com',
     'loadtestsinfo@gmail.com',
     'straightwaytest@gmail.com',
     'test.of.tests@gmail.com',
     'bigmac@gmail.com',
     'bigmactest@gmail.com',
     'kfc_test_supply@gmail.com',
     'cyberdesk@gmail.com',
     'supportonlinetest@gmail.com'
     ]

k = []
for i in l:
     if 'test' in i:
          k.append(i)
print(k)
print(l)

____________________________________________

# 5. найти самое маленькое число в списке
l = [3,0,4,5,8,9,10,44,22,50,-1,79,54,-28,91]

min = l[0]
for i in l:
    if i < min:
        min = i
print(min)

# САМЫЙ ПРОСТОЙ СПОСОБ: !!!!!! 
print(min(l))

___________________________________________
# 6. Сравнить 2 строки без учёта регистра

s1 = 'alexander'
s2 = 'aleXanDeR'

# s1 и s2 явялются идентичными (сделать сравнение об этом)
# Функции для решения: upper и lower (переводят строку соответственно в верхний и нижний регистры)

if s1.lower() == s2.lower():
    print(True)
else:
    print(False)

# Самое простой решение:

print(s1.lower() == s2.lower())
________________________________________

# 7. Проверить является ли массив подмножеством (элементы одного массива в любом порядке есть в другом массиве)
# другого массива

l1 = [1,4,6]
l2 = [9,5,1,10,4,33,2,6,0,8]

c = 0
for i in l1:
    if i in l2:
        c +=1
if c==len(l1):
    print(True)
else:
    print(False)

____________________________________________

# 8. Напишите функцию, которая принимает строку и возвращает количество букв английского алфавита, которые встречаются больше чем 1 раз.

s = 'july'
# count = 0
abc = 'qwertyuiopasdfghjklzxcvbnm'

for i in abc:
    count = 0
    for j in s:
        if j == i:
           count +=1
    if count >1:
        print(i, 'встречается', count, 'раз')
 ______________________________________________________

