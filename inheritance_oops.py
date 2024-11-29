##inheritance:
##
##5 type of inheritance have in python:
##
##that is:
##
##1.single inheritance,
##2.multiple inheritance,
##3.multilevel inheritance,
##4.hyrarichal inheritance,
##5.hybrid inheritance.
##
##1.single inheritance:

class dad():
    def mind(self):
        print("Dad mind")

class son(dad):
    def kind(self):
        print("my kind is my positive and")
me=son()
me.kind()
me.mind()

##2.multiple inheritance:

class dad():
    def mind(self):
        print("Dad mind")

class mom():
    def love(self):
        print("mom's love")

class son(dad,mom):
    def kind(self):
        print("my kind is my positive and")
me=son()
me.kind()
me.mind()
me.love()

##3.multilevel inheritance:
class grandpa():
    def assets(self):
        print("grandpa's assets")

class dad(grandpa):
    def business(self):
        print("Dad's business")

class son(dad):
    def kind(self):
        print("my kind is my positive thats all")

me=son()
me.assets()
me.business()
me.kind()

##4.hyrarical inheritance:
class dad():
    def money(self):
        print("take my money my sons")
class son1(dad):
    def kind(self):
        print("son1 he is more kind")
class son2(dad):
    def attitude(self):
        print("son1 he is more kind")     
class son3(dad):
    def strenth(self):
        print("son1 he is more kind")

me=son1()
me.kind()
me.money()

##hybrid():



