# ------ hash method ----- how its runn....
print(hash("mani"))
#this hash map give a one value  that is (4644169627606722112)
# and run again print("mani") statement that is return the different value (81842174250153080)
# every time you run and get different value but,
print(hash("mani"))
print(hash("mani")) #run two print statement is same time return the value is same 
# 7727166489213030476
# 7727166489213030476 because this two print stement is run in same "session" same session la 
# enakku two print statement run aguthu

# HaspMap implementation

class HashMap:
    
    def __init__(self,size):
        self.size=size
        self.hashIndex=