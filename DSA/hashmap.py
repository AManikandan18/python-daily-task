# ------ hash method ----- how its runn....

# print(hash("mani"))

#this hash map give a one value  that is (4644169627606722112)
# and run again print("mani") statement that is return the different value (81842174250153080)
# every time you run and get different value but,

# print(hash("mani"))
# print(hash("mani")) #run two print statement is same time return the value is same 

# 7727166489213030476
# 7727166489213030476 because this two print stement is run in same "session" same session la 
# enakku two print statement run aguthu

# HaspMap implementation

class HashMap:
    
    def __init__(self,size):
        self.size=size
        self.hashIndex=[None]*self.size

    def get_index(self,key):
        return hash(key)%self.size
    
    def __setitem__(self,key,value):
        index=self.get_index(key)
        print(index)
        if self.hashIndex[index] is None:
            self.hashIndex[index]=[[key,value]]
            print(self.hashIndex)
        else:
            self.hashIndex[index].append([key,value])
            print(self.hashIndex)

    def Get(self,key):
        index=self.get_index(key)
        if self.hashIndex[index]:
            for val in self.hashIndex[index]:
                if val[0]==key:
                    print(val[1])
        else:
            print("your value" ,key,"is not here")
        
    
obj=HashMap(10)
# obj.hashIndex
# obj.add("name","mani")
# obj.add("age",18)
obj["roll"]="2026J09" #this code for when you using the bild-in-function def __setitem__():
obj.Get("roll")
# obj["roll"]="2026J09"
# obj.Get("roll")
