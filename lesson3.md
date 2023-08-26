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
