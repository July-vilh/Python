# ЗАДАЧИ

# ЗАДАЧА 1. ВЫВЕСТИ В КОНСОЛЬ ТАБЛИЦУ УМНОЖЕНИЯ (МАТРИЦУ)

i = 1
n = 1

#надо сделать что бы было написано: результат умножения - пробел - новая строчка - результат умножения - пробел и т.д. (проумножать 10 цифр)

while i < 10:
while n < 10:
  
  result = i * n
  
  print(result, end="\t")
  
  n += 1
  
# end= переводится как "в конце поставь вот это" 
# \t переводится как "ТАБ" (каждое окончание записи будет ставить ТАБ) = ПРОМНОЖИЛИ СТРОКУ: РЕЗУЛЬТАТ - ТАБ; РЕЗУЛЬТАТ - ТАБ

# i ИДЕТ ПО ГОРИЗОНТАЛИ
# n идет по ВЕРТИКАЛИ
# от result до n+=1 это тело цикла, которое принадлежит while n < 10

# ТЕПЕРЬ ЧТО БЫ БЫЛО ПО ВЕРТИКАЛИ НАДО 1, ПОТОМ 2 ПРОМНОЖИТЬ (В ПЕРВОМ ЦИКЛЕ while i < 10):

i += 1
n = 1
print("\n")

# \n переводится как "ПЕРЕСКОКНИ НА СЛЕДУЮЩУЮ СТРОКУ" (ДАННОЕ ТЕЛО ЦИКЛА ОТНОСИТСЯ К while i < 10;)

# КАК ИТОГ ПОЛНЫЙ КОД (ВСЕ ВМЕСТЕ С ОТСТУПАМИ И ВЛОЖЕННОСТЯМИ В ЦИКЛ):

i = 1
n = 1

while i < 10:
  while n < 10:
    result = i * n
    print(result, end="\t")
    n += 1

  i += 1
  n = 1
  print("\n")
  
# РЕЗУЛЬТАТ: 

# 1	2	3	4	5	6	7	8	9	

# 2	4	6	8	10	12	14	16	18	

# 3	6	9	12	15	18	21	24	27	

# 4	8	12	16	20	24	28	32	36	

# 5	10	15	20	25	30	35	40	45	

# 6	12	18	24	30	36	42	48	54	

# 7	14	21	28	35	42	49	56	63	

# 8	16	24	32	40	48	56	64	72	

# 9	18	27	36	45	54	63	72	81	
_____________________________
jj;k;lk
