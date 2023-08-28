## OOP

### 1) Create human with any parameters and then create function:
```
class Human:
    def __init__(self, name, sex, years, height, weight):
        self.name = name
        self.sex = sex
        self.years = years
        self.height = height
        self.weight = weight

    def walk(self):
        print(f'{self.name} walk')


Yuliya = Human(name='Yuliya', sex='female', years=25, height=165, weight=45)
Vlad = Human(name='Vlad', sex='male', years=26, height=165, weight=60)
Yuliya.walk();
Vlad.walk();

print(Yuliya.sex)

```
> RESULT: Yuliya walk
> Vlad walk
> female


### 2) @staticmethod (for parameters, which no at the "self" parameters):
 
```
class Human:
    def __init__(self, name, sex, years, height, weight):
        self.name = name
        self.sex = sex
        self.years = years
        self.height = height
        self.weight = weight

    @staticmethod
    def speak(word):
        print(word)
  Yuliya = Human(name='Yuliya', sex='female', years=25, height=165, weight=45)

  Yuliya.speak('I am Yulya')

```
> RESULT: I am Yulya

### 3) @classmethod (for display class (create)):

```
class Human:
    def __init__(self, name, sex, years, height, weight):
        self.name = name
        self.sex = sex
        self.years = years
        self.height = height
        self.weight = weight

  @classmethod ////create our Human
    def birth(cls, name, sex, years, height, weight):
        return cls(name, sex, years, height, weight)

  def __repr__(self):
        return f'Human consists: name = {self.name}, sex = {self.sex}, years = {self.years}, height = {self.height}, weight = {self.weight}'

Sirius = Human.birth(name='Sirius', sex='male', years=1, height=30, weight=5)
print(Sirius)

```
> RESULT: Human consists: name = Sirius, sex = male, years = 1, height = 30, weight = 5

### 4) New method (which no in parameters of class) with CONDITIONS (if/else):

```
class Human:   /////// our class
    def __init__(self, name, sex, years, height, weight):
        self.name = name
        self.sex = sex
        self.years = years
        self.height = height
        self.weight = weight

   def run(self):         /// our function with conditions (if/else)
      if self.years > 3:
        return print(f'{self.name} run!')
      else:
        return print(f'{self.name} can not run!')


  //// our people:
  Yuliya = Human(name='Yuliya', sex='female', years=25, height=165, weight=45)
  Vlad = Human(name='Vlad', sex='male', years=1, height=165, weight=60)

  Vlad.run()
  Yuliya.run()

```
> RESULT: Vlad can not run!
> Yuliya run!

### 5) any example (auto):

```
class Auto:
    def __init__(self, mark, type):
        self.mark = mark
        self.type = type

    def drive(self):
        print(f'{self.mark} drive')

mini_couper = Auto(mark='mini_couper', type='sedan')
mini_couper.drive()

rzug = Auto(mark='rzug', type='sedan')
rzug.drive()
```
> RESULT: mini_couper drive
> rzug drive
