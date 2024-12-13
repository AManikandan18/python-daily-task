##"""super keyword is used to inherit the parent class and mainly used to namma oru
##3 class ha create pannitu mela ulla 2 class kku init use pannitu then andha rendu(2)
##class ha yum moonavathu(third) class la inherit pannumpothu third class la
##__init__() method use pannirundha andha oru __init__() method tha print agum so
##we use the super().__init__() method inherit panna class la ha __init__()
##irundha adhayum sethu print pannum that is reason to we use the super().__init__()
##function"""
##
##
##class a():
##    def __init__(self):
##        print("class A")
####        super().__init__()
##    def display(self):
##        print("calss a is display")
##
##class b():
##    def __init__(self):
##        super().__init__()
##        print("class b")
##    def display(self):
##        print("calss b is display")
##
##class c():
##    def __init__(self):
##        print("class c")
##        super().__init__()
##    def display(self):
##        print("class c is display")
##
##class d():
##    def __init__(self):
##        super().__init__()
##        print("class d")
##    def display(self):
##        print("calss d is display")
##
##class e(d,c,b,a):
##    def __init__(self):
##        super().__init__()
##        print("class e")
##    def display():
##        print("calss e is display")
##
##
##obj2=e()
#### mro used to see the (orderwise) or see chaining class if you create a all function in same name:  
##print(e.__mro__)
#### another way to call mro:
##print(e.mro())
##
####super function example or exercise:
####class mani():
####    def __init__(slef):
####        print("class mani")
####    def inits(self):
####        print("inits methods")
####
####class nandhu(mani):
####    def __init__(self):
####        super().__init__()
####        print("class nandhu is print")
####    def inits2(self):
####        print("inits2 methods")
####obj=nandhu()
####
##

##class A:
##    def __init__(self):
##        a=10
##        print(a)
##class B(A):
##    def __init__(self):
##        super().__init__()
##        a=20
##        print(a)
##class C(A):
##    def __init__(self):
##        super().__init__()
##        a=30
##        print(a)
##
##class D(C,B):
##    def __init__(self):
##        super().__init__()
##        a=40
##        print(a)
##obj=D()

class A:
    pass
class B(A):
    pass
class D(B):
    pass
class C(A,D,B):
    def name(self):
        print("mani")
##class D(C,B,A):
##    pass
    
obj=C()
obj.name()
