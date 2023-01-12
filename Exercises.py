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
# s1 = 'alexander'
# s2 = 'aleXanDeR'
# s1 и s2 явялются идентичными (сделать сравнение об этом)
