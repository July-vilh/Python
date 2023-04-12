> ------------ 1)This code should store "codewa.rs" as a variable called name but it's not working. Can you figure out why?

```
a == "code"
b == "wa.rs"
name == a + b
```

> SOLUTION

```
a = "code"
b = "wa.rs"
name = a + b
``` 

RESULT: codewa.rs
==========================================================================================================================

> --------------- 2) Make a simple function called greet that returns the most-famous "hello world!".

Style Points

Sure, this is about as easy as it gets. But how clever can you be to create the most creative "hello world" you can think of? What is a "hello world" solution you would want to show your friends?

``` 
def greet():
    return "hello world!"
``` 

RESULT: hello world!

==========================================================================================================================

> --------------- 3) Write a function that will accept two parameters: variable and type and check if type of variable is matching type. Return true if types match or false if not.

``` 
def type_validation(variable, _type): 
    return _type in str(type(variable))
``` 

========================================================================================================================

> --------------- 4) Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.

``` 
def boolean_to_string(b):
    return str(b)
``` 

==========================================================================================================================

> ---------------- 5) Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)

6, "I"     -> "IIIIII"

5, "Hello" -> "HelloHelloHelloHelloHello"

``` 
def repeat_str(repeat, string):
    return repeat * string
``` 

==========================================================================================================================

> -------------- 6) The goal is to create a function of two inputs number and power, that "raises" the number up to power (ie multiplies number by itself power times).

Examples

``` 
number_to_pwr(3, 2)  # -> 9 ( = 3 * 3 )
number_to_pwr(2, 3)  # -> 8 ( = 2 * 2 * 2 )
number_to_pwr(10, 6) # -> 1000000
``` 

> SOLUTION:

``` 
def number_to_pwr(number, p): 
    num = 1
    for i in range(p):
        num *= number
    return num
``` 

=========================================================================================================================

> -------------- 7) 
