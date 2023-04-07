1) Метод Replace = возвращает копию исходной строки, в которых строки которые мы хотим изменить заменяяются на новые. 

```
s = 'Hello world'
print (s.replace('e', 'a'))
```

РЕЗУЛЬТАТ:

Hallo world

Шаблон для метода Replace: s.replace(old value, new value, count)

- old value = старое конкретное значение, которое мы хотим поменять
- new value = новое значение, которое мы хотим придать старому (на что заменить)
- count = количество значений (старых) которые будут подвергаться замене на новые (НЕОБЯЗАТЕЛЬНО)

```
s = 'Hello world'
print (s.replace('l', '?', 2))
```

РЕЗУЛЬТАТ: He??o world

```
s = 'Hello world'
print (s.replace('l', '?', 3))
```

РЕЗУЛЬТАТ: He??o wor?d

```
s = 'Hello world'
print (s.replace('l', '?'))
```

РЕЗУЛЬТАТ: He??o wor?d
