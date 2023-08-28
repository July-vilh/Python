## LOOPS ("For", "While")

### LOOP "FOR" (for list, tuple, set, dictionary)
The "FOR" loop goes on until something ends

```
name = 'Artur'

def toxic_function(name):
    match name:
        case 'Ivan':
            printing_message(name)
        case 'Artur':
            printing_message(name)
        case 'Nikita':
            printing_message(name)
        case _:
            print('Fuck u')


names = ['Alex', 'Ivan', 'Artur', 'Nikita']
for name in names:
    toxic_function(name)
```
> RESULT: Fuck u; fuck you, Ivan!; fuck you, Artur!; fuck you, Nikita (the lop is break after goon all names)

#### For DICTIONARY:

1) For keys in Dictionary:

```
from pack.module1 import toxic_function

names = {'Alex': 3, 'Ivan': 2, 'Artur': 1, 'Nikita': 0}
for name in names.keys():
    toxic_function(name)
```
> RESULT: Fuck u; fuck you, Ivan!; fuck you, Artur!; fuck you, Nikita

2) For values in dictionary:

```
from pack.module1 import toxic_function

names = {'Alex': 3, 'Ivan': 2, 'Artur': 1, 'Nikita': 0}
for name in names.values():
    toxic_function(name)
```
> RESULT: Fuck u; Fuck u; Fuck u; Fuck u



### LOOP "WHILE"
the "While" loop = continues until a certain condition is met

```
name = 'Artur'

def toxic_function(name):
    match name:
        case 'Ivan':
            printing_message(name)
        case 'Artur':
            printing_message(name)
        case 'Nikita':
            printing_message(name)
        case _:
            print('Fuck u')


name = None
while name != 'Nikita':
    name = input('Enter your name:  ')
    toxic_function(name)
```
> RESULT: 1) if input name = Nikita: Enter your name:  Nikita => fuck you, Nikita! (the loop is stop because Nikita = Nikita)
> 2) if input name != Nikita: Enter your name:  Yulya => fuck u (the loop is not stop because Nikita != Yulya)

