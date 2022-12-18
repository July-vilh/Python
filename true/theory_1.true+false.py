# 1. True/False (0=false; 1=true)
item_1 = 1;
item_0 = 0;

name = 'July'
name_e = ''

none_item = None

items_list = ['11', 22]
items_list_e = []

b_item_t = True;
b_item_f = False;

if item_1:
    print('True item')
else:
    print('False item')

# Логика: Если существует этот элемент (item_1) и у него есть какое-то значение, то выполняется элемент кода
# print('True item').
#__________
if item_0:
    print('True item')
else:
    print('False item')

# результат false_item потому что item_0 это 0 (false)
#__________
if name:
    print('True item')
else:
    print('False item')

if items_list:
    print('True item')
else:
    print('False item')
#наличие хоть чего-то в строке это уже True.
#____________

if items_list_e:
    print('True item')
else:
    print('False item')
#false потому что переменная пуста и ничего не содержит (0)
#_____________

if name_e:
    print('True item')
else:
    print('False item')
#false потому что переменная пуста и ничего не содержит (0). Если вставить пробел то будет уже True тк пробел это
#уже символ
#______________

if none_item:
    print('True item')
else:
    print('False item')
#false тк тип None
#_________
if b_item_t:
    print('True item')
else:
    print('False item')
#ответ true (тк переменная содержит тип true)
#______________

if b_item_f:
    print('True item')
else:
    print('False item')
#ответ false (тк переменная содержит тип false)
#___________________

#COMPARE (СРАВНЕНИЕ)
compare_item = item_1 > item_0
#результатом таких выражений всегда будет либо ложь либо истина. Если item_1 действительно больше item_0 то
#будет истина. Если же наоборот то будет false.

if compare_item:
    print('True item')
else:
    print('False item')
#______________________
item_2 = 1
item_3 = 10

compare_item_1 = item_2 > item_3

if compare_item_1:
    print('True item')
else:
    print('False item')
#результатом будет false тк 1 не больше 10
#____________________

item_4 = 1
item_5 = 1

compare_item_2 = item_4 == item_5

if compare_item_2:
    print('True item')
else:
    print('False item')
# результат истина потому что 1 строго равно 1
#___________________

item_6 = 1000
item_7 = 122

compare_item_3 = item_6 >= item_7

if compare_item_3:
    print('True item')
else:
    print('False item')
#результат false тк 10 не больше и не равно 122
#____________

#ELIF = ИНАЧЕ ЕСЛИ

if compare_item_3:
    print('----1---- True item')
elif name:
    print('---- 2 ---- Name item')
elif items_list:
    print('---- 3 ---- items_list')
elif 10 > 20:
    print('---- 4 ----- items_list')
else:
    print('-------False item')
# Логика elif: если хоть одно условие отработало, то дальше ничего не отрабатывает даже если остальные условия тоже
# истины. Ищет пока не нарвется на истину (true)
#___________________________

#ВЛОЖЕННЫЕ IF:
if compare_item_3:
    print('----- 1 ----- True item')

    if b_item_t:
        print('inner IF -- 1 --- True item')
#результат 2 этих варианат тк у них обоих истинные условия
#_______________________________

#ОБЪЯВЛЕНИЕ ПЕРЕМЕННЫХ ВНУТРИ IF:
if compare_item_3:
    print('----- 1 ----- True item')

    new_name = 'natalia'
    user_age = 30
    print('user_age', user_age)

    if new_name:
        new_user_age = user_age - 5
        print('new_user_age', new_user_age)
#Если первый if не выполняется (не истина), то глубже мы не войдем (остальное не выполнится)
#_________

#ВОССОЗДАНИЕ НЕСКОЛЬКИХ УСЛОВИЙ СРАЗУ (ЧЕРЕЗ И/ИЛИ):
if compare_item_3 & b_item_t:
    print('----- 1 ----- True item')

if compare_item_3 or b_item_f:
    print('----- 1 ----- True item')

if compare_item_3 and b_item_t and items_list:
    print('----- 1 ----- True item')

if compare_item_3 and b_item_t or items_list:
    print('----- 1 ----- True item')
#_______________

#NOT (НЕ)
item_8 = 6
item_9 = 7

compare_item_4 = item_9 < item_8
#тут false

if not compare_item_4:
    print('--- 2 --- compare_item_4')

#Если не false то будет истина (true): not+true = кусочек кода не выполнится и not+false = выполнится
#__________________

#ЦИКЛ НА ВЫВОД ТОЛЬКО ЧЕТНЫХ ЭЛЕМЕНТОВ ИЗ ОПРЕДЕЛЕННОГО ДИАПАЗОНА (через тернарный оператор т.е. 1 строку):
list_items = [result for result in range(0,100) if result % 2 == 0]
for ii in list_items:
    print('% result = ', ii)

#Цикл полноценный (не в 1 строку):

list_items_1 = []
for result in range(0,100):
    result_odd = result % 2

    if result_odd == 0:
        list_items_1.append(result)
