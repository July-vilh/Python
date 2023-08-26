## FUNCTIONS


```
name = 'Artur'

def hello():
    print('Fuck u')

match name:
    case 'Ivan':
        hello()
    case 'Artur':
        hello()
    case 'Nikita':
        hello()
    case _:
        print('Fuck u')
```
> RESULT: Fuck u (there we replace "print('Fuck u")" to the function "hello()" where we can just change print('...') only for finction (not for all code))

### FUNCTION + parameters of function (for example "Hello, <name>") with COMPETINATION

```
name = 'Artur'

def hello(name):
    message = 'Hello, ' + name + '!'
    print(message)


match name:
    case 'Ivan':
        hello(name)
    case 'Artur':
        hello(name)
    case 'Nikita':
        hello(name)
    case _:
        print('Fuck u')
```
> RESULT: Hello, Artur!

### FUNCTION + parameters of function (for example "Hello, <name>") with FORMATTING a string

```
def hello(name):
    message = f'Hello, {name}!'
    print(message)


match name:
    case 'Ivan':
        hello(name)
    case 'Artur':
        hello(name)
    case 'Nikita':
        hello(name)
    case _:
        print('Fuck u')
```

> RESULT: Hello, Artur!

### FUNCTION in FUNCTION:

```
name = 'Artur'

def create_message(name):
    message = f'Hello, {name}!'
    return message

def printing_message(name):
    message=create_message(name)
    print(message)
match name:
    case 'Ivan':
        printing_message(name)
    case 'Artur':
        printing_message(name)
    case 'Nikita':
        printing_message(name)
    case _:
        print('Fuck u')
```
> RESULT : Hello, Artur!
