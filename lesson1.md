## Types of data in Python
1. int (integer)
2. str (string) = 'any data'
3. tuple = (1, 2, 3) only for storing values and does not allow these values to be deleted!!! some @safe@ for counting or getting index
4. list
5. dict
6. set
7. float

1) Sum (method = __add__) for INTEGER (1):

```
a = 1
b = a.__add__(2)
print(b)
```
RESULT: 3 (b=1+2)

same:

```
a = 1
b = a + 2
print(b)
```
RESULT: 3 (b=1+2)

2) FOR STRING:

```
a = 'word'
b = a.__add__('word2')
print(b)
```
RESULT: wordword2

------- same: 

```
a = 'word'
b = a + 'word2'
print(b)
```
RESULT: wordword2

```
a = 'word'
b = a * 3
print(b)
```
RESULT: wordwordword

----------- all latters in word to do in CapsLock:

```
a = 'word'
b = a.upper()
print(b)
```
RESULT: WORD

3) sum for TUPLE (counting a selected quantity):

```
a = (1, 2, 3)
b = a.count(2)
print(b)
```
RESULT: 1

4) 

