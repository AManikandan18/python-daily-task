##class laptops:
##    price="10000"
##    processor="i?"
##    ram="gb"
##    def hp(self):
##        print("hp laptop")
##    def lenovo(self):
##        print("lenovo laptop")
##    def dell(self):
##        print("dell laptop")
##
##
##hp=laptops()
##hp.price="40000"
##hp.processor="i5"
##hp.ram="500gb"
##print(hp.price)
##print(hp.processor)
##print(hp.ram)
##
##lenovo=laptops()
####same process to lenovo
##dell=laptops()
####same process to dell

##

##constructor and self method:
class person:
    def __init__(self):
        print("defualt printing messeges")
        self.name=""
        self.age=0
        self.year=0
    def biodata(self):
         
        print("your name: ",self.name)
        print("your age is: ",self.age)
        print("your date of birth is: ",self.year)

person1=person()
person1.name="mani"
person1.age=18
person1.year=2006

person1.biodata()

##constructor with pass parameter:
class fruit:
    def __init__(self,color,name,price):
        self.color=color
        self.name=name
        self.price=price
f1=fruit("orange","orange",350)      
        
