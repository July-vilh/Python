## MODULES and PACKAGES

Modules are files with the ".py" extension that contain code that can be used in other parts of the program (module = file, which contains smth functions).
Packages are a way to organize related modules in one place.

## 1) MODULES:
### module with code:

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

### application with code (import data from module):

```
import module
print(module.create_message('Ivan'))
```
> RESULT: in module = "Hello, Artur!" and in application = "Hello, Artur!" + "Hello, Ivan!"

### for in application = only "Hello, Ivan!" need add "if __name__ == '__main__':" construction after all functions at the module code 4

```
name = 'Artur'

def create_message(name):
    message = f'Hello, {name}!'
    return message

def printing_message(name):
    message=create_message(name)
    print(message)

if __name__ == '__main__':

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
> RESULT: in module = "Hello, Artur!" and in application = "Hello, Ivan!"

### if you need only 1 function (not all module) you can do import for this 1 fuction (not all module):

### code (application):

```
from module import create_message
print(create_message('Ivan'))
```
> RESULT: Hello, Ivan!

### if you have 2 different modules, for solve problems you can add to the function aliases:

```
from module import create_message as hello
from module1 import create_message as fuck
print(hello('Ivan'))
print(fuck('Alex'))
```

> RESULT: "Hello, Ivan!" + "fuck you, Alex!"

## 2) PACKAGE 
### package after create = consists empty file init.py anf=d then you can do file (.py) transfer to the package 

> RESULT (code at the application after transfer modules to the package):

```
from pack.module import create_message as hello
from pack.module1 import create_message as fuck
print(hello('Ivan'))
print(fuck('Alex'))
```

