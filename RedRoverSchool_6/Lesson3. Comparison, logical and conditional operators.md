---------------------------------------------------- ОПЕРАТОРЫ СРАВНЕНИЯ --------------------------------------------------------------

### РАВЕНСТВО (==)
### НЕРАВЕНСТВО (!=)
### МЕНЬШЕ (<)
### МЕНЬШЕ ИЛИ РАВНО (<=)
### БОЛЬШЕ (>)
### БОЛЬШЕ ИЛИ РАВНО (>=)

ЭТИ ОПЕРАТОРЫ ВОЗВРАЩАЮТ БУЛЕВЫЕ ЗНАЧЕНИЯ: TRUE ИЛИ FALSE

------------------------------------------------- ЛОГИЧЕСКИЕ ОПЕРАТОРЫ ---------------------------------------------------------------
## 1) AND
## 2) OR
## 3) NOT

УСЛОВИЕ: X = 5. ЭТИ ОПЕРАТОРЫ ТАКЖЕ ВОЗВРАЩАЮТ БУЛЕВЫЕ ЗНАЧЕНИЯ: PRUE ИЛИ FALSE

## AND
### 1. X > 3 AND X < 8 (TRUE/FALSE) TRUE
### 2. X > 3 AND X > 8 (TRUE/FALSE) FALSE

```
x = 5
print (x < 3 and x > 8)
```

## OR 
### 1. X > 3 OR X < 8 (TRUE/FALSE) TRUE
### 2. X > 3 OR X > 8 (TRUE/FALSE) TRUE
### 3. X < 3 OR X > 8 (TRUE/FALSE) FALSE

## NOT 
### 1. NOT X > 5 (TRUE/FALSE) TRUE
### 2. NOT X == 5 (TRUE/FALSE) FALSE
### 3. X > 3 AND NOT X > 8 (TRUE/FALSE) TRUE
### 4. X < 3 AND NOT X < 8 (TRUE/FALSE) FALSE 



------------------------------------------------ УСЛОВНЫЕ ОПЕРАТОРЫ --------------------------------------------------------------------------

#### ОПЕРАТОР IF (Если да - то пиши...) для ПЕРВОГО варианта
#### ОПЕРАТОР ELSE (Если нет - то пиши...) для ВТОРОГО если только 2 условия и для ПОСЛЕДНЕГО если больше 2 условий

```
num = 5
if num == 5:
    print ('five')
else:
    print('not equal five')

```
### ОПЕРАТОР ELIF (Else If) для ПРОМЕЖУТОЧНОГО оператора если больше 2 условий 

```
num = 5
if num == 5:
    print ('five')
elif num > 5:
    print ('more than five')
else:
    print('less than five')
```

### ПРОВЕРКА ВОЗРАСТА ПОСЕТИТЕЛЯ

```
age = int(input('Please, enter your age: '))
if age >= 18:
    print('Welcome!')
else:
    print('Go home, baby!')
```

---------------------------------------------------- ПРЕОБРАЗОВАНИЕ ОШИБКИ ПАЙЧАРМА В ЧЕЛОВЕЧЕСКУЮ (try - except) -----------------------

```
num1 = int(input('Please, enter first number: '))
num2 = int(input('Please, enter second number: '))
operator = input('Please, enter operator: ')
try:
    result = num1 / num2
    print(f'Результат: {result}')
except ZeroDivisionError:
    print('На ноль делить нельзя!')
```

```
num1 = int(input('Please, enter first number: '))
num2 = int(input('Please, enter second number: '))
operator = input('Please, enter operator: ')
if num2 == 0 or operator == '/':
    try:
        result = num1 / num2
        print(f'Результат: {result}')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
else:
    result = num1 * num2
    print(f"Результат: {result}")
```


--------------------------------------------- ВЫ ВВЕЛИ НЕ ЧИСЛО (ПРЕОБР. ОШИБКИ) ---------------------------------------------------

```
try:
    num1 = int(input('Please, enter first number: '))
    num2 = int(input('Please, enter second number: '))
except ValueError:
    print('Вы ввели не число!')
    operator = input('Please, enter operator: ')
if num2 == 0 or operator == '/':
    try:
        result = num1 / num2
        print(f'Результат: {result}')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
else:
    result = num1 * num2
    print(f"Результат: {result}")
```


---------------------------- БИБЛИОТЕКА sys ОБ ОКОНЧАНИИ ДЕЙСТВИЯ КОДА -----------------------------------------------------------------

```
import sys
try:
    num1 = int(input('Please, enter first number: '))
    num2 = int(input('Please, enter second number: '))
except ValueError:
    print('Вы ввели не число!')
    sys.exit()
    operator = input('Please, enter operator: ')
```

