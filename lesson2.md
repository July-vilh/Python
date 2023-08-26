## "if" and "match"

Program flow control allows us to control which parts of the code will be executed depending on various conditions.  The "if" statement allows you to check conditions and execute various blocks of code depending on whether the condition is met or not. 
The "match" operator is a new operator in Python 3.10 that provides a new way to match values and execute different blocks of code depending on the match.

```
name = 'Alex'

if name == 'Ivan':
    print('Hello')
else:
    if name == 'Artur':
        print('Hello')
    else:
        if name == 'Nikita':
            print('Hello')
        else:
            print('Fuck u')
```
> RESULT: Fuck u

This code is better:

```
name = 'Ivan'

if name == 'Ivan':
    print('Hello')
if name == 'Artur':
    print('Hello')
if name == 'Nikita':
    print('Hello')
else:
    print('Fuck u')
```
> but there after name == 'Ivan' => program is not stop and go + as a result: 'Hello' 'Fuck u'

