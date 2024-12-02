"""super keyword is used to inherit the parent class and mainly used to namma oru
3 class ha create pannitu mela ulla 2 class kku init use pannitu then andha rendu(2)
class ha yum moonavathu(third) class la inherit pannumpothu third class la
__init__() method use pannirundha andha oru __init__() method tha print agum so
we use the super().__init__() method inherit panna class la ha __init__()
irundha adhayum sethu print pannum that is reason to we use the super().__init__()
function"""


class a():
    def __init__(self):
        print("class A")
    def display(self):
        print("calss a is display")

class b():
    def __init__(self):
        super().__init__()
        print("class b")
    def display(self):
        print("calss b is display")

class c():
    def __init__(self):
        print("class c")
        super().__init__()
    def display(self):
        print("class c is display")

class d():
    def __init__(self):
        super().__init__()
        print("class d")
    def display(self):
        print("calss d is display")

class e(a,b,c,d):
    def __init__(self):
        super().__init__()
        print("class e")
    def display():
        print("calss e is display")


obj2=e()
## mro used to see the (orderwise) or see chaining class:  
print(e.__mro__)


