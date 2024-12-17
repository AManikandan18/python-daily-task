## stack is like 3 floor cake if you want to take first floor cake you cut the
## top two floor cake first then you take the first floor.

## stack is have a 5 types it is:
##1.push(append)
##2.pop
##3.peek([-1]) ,because peek is view the last value in the list
##4.size[len()],
##5.isempty(items==[])

## stack data structure:
class stack():
    def __init__(self):
        self.__item=[1,2,3]
        
    def push(self,value):
        self.item.append(value)
        print(self.__item)
        
    def pop_value(self):
        if self.__item:
            self.__item.pop()
            return self.item
        
    def peek_value(self):
        if self.item:
            return self.__item[-1]
        
    def sizes(self):
        if self.__item:
            return len(self.__item)
        
    def isempty(self):
        if self.__item==[]:
            print(True)
        else:
            print(False)

obj=stack()
##obj._stack__item.clear() #ippadi potta enakku print aguthu but i use the private modifier

obj.__item.clear() # ithula enakku error varuthu.
obj.isempty()

##Why the Error Occurs:
##When you try to access obj.__item.clear() from outside the class, Python doesn't find __item because it has been renamed to _stack__item. This leads to the AttributeError.

## queue data structure:

##class queue:
##    def __init__(self):
##        self.item=[1,2,3]
##    def enqueue(self,item):
##        self.item.append(item)
##        print(self.item)
##    def dequeue(self):
##        self.item.pop(0)
##
##    def peek(self):
##        if self.item:
##            return self.item[-1]
##        
##    def item_size(self):
##        if self.item:
##            return len(self.item)
##    def isempty(self):
##        if self.item==[]:
##            return True
##        else:
##            return False    
##obj=queue()
##obj.enqueue(10)




##from array import *
##
##arr=array('i',[])
##n=int(input())
##for i in range(n):
##    x=int(input())
##    arr.append(x)
##print(arr)
##    