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

class animal():
    def sound(self):
        print("animal make sound")

class pets():
    def sound(self):
        print("dog make noice")
    def satham(self):
        print("ore satham")

class bird(pets,animal):
    def sound(self):
        print("bird sing")  

b1=bird()
b1.satham()
