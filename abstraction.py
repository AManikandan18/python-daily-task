from abc import ABC,abstractmethod
class Shapes(ABC):
    @abstractmethod
    def pent(self):
        pass
    @abstractmethod
    def hex(self):
        print("hi welcome")
class Shape(Shapes):
    def pent(self):
        print("i have four sides")
    def pen(self):
        print("i have four sides")    
class Shap(Shapes):
    def pent(self):
        print("i have five sides")
obj1=Shape()
obj1.pen()
obj2=Shap()
obj2.pent()
#abstract method ha object creat panni call panna mudiyathu: 
obj2.hex()

#this is
