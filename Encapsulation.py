## Encapsulation:

## Content:


## Access Modifier:

## 1.Public coding:
class manager():
    def __init__(self):
        self.name="mani"
    def show(self):
        print(self.name)
m1=manager()
m1.show()
## And Public in disadvandages is public na enna la veliya irundhu value change
## pannalam example is:
m1.name="mass"
print("Ennala value ha outside irundhu cange panna mudiyuth so this is disadvandage",m1.name)

## 2.Private Coding:

## Private is only use within the same class functions:

class manager1():
    def __init__(self):
        self.__name="this is the protect name mani"
        
    def show(self):
        print(self.__name)
m1=manager1()
m1.show()

## Protect is can i use the variable value in the subclass(Inheritance):

## 3.Protect Coding:
class manager():
    def __init__(self):
        self._name="mani"
    def show(self):
        print("my name is ",self._name)

class manager1(manager):
    def show1(self):
        print("hi what's your name :",self._name)
m1=manager1()
m1.show1()
        
        
