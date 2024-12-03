## polymorphism :

##* polymorphism is overriding in python.
##* polymorphism means many ways to solve one problem.
##* polymorphism is used to enakku ore function la 2 argument ha pass pannalum
##  andha numbers add(+) agi enakku output varanum and adhe function la 3
##  argument pass pannalum enakku output varanum that is called (same name
##  but different signature).
##  

## 1 Way:
##This way is called same function but different singnature:

def display(a,b,c=5):
    print(a+b+c)
display(5,5) #na first rendu(2) value va argument ha pass pandrappavum enakku
             #program run agi output varanum and...

display(10,10,10) #moonu argument ha pass pannum pothum enakku three values hum
                  #add agi output varanum.

## Second Way:

## second way la na enna pandrana three class open pandra but ulla irukka ella
## function kkum na name sound nu vaikkiren so python interpretor first sound
## function ha pakkuthu then second sound function ha pakkuthu so adha override
## pannuthu then third sound function ha pakkthu aprom adha override panni adha
## print pannuthu...

class animal():
    def sound(self):
        print("animal make sound")

class pets():
    def sound(self):
        print("dog make noice")

class bird(pets,animal):
    def sound(self):
        print("bird sing")  

b1=bird()
b1.sound()


##polymorphism task by EMC academy:
print("polymorphism tasks")
class employee():
    def __init__(self,name,salary):
        print("hello")
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,department="it"):
        super().__init__(name,salary)
        self.department=department
        
    def display(self):
        print("Hi my name is :",self.name,"salary is",self.salary,"my department is",self.department)
        
m1=manager("mani",100000,"technology")
m1.display()

