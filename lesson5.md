## LOOPS ("For", "While")

### LOOP "FOR"
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
> RESULT: Fuck u; fuck you, Ivan!; fuck you, Artur!; fuck you, Nikita 9the lop is break after goon all names)




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

