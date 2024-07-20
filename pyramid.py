n=5
for i in range(n):
    print("")
    for j in range(n):
        print("*",end=" ")
        
rows=int(input("enter the rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
        
rows=int(input("enter the rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()        

rows=int(input("enter the rows: "))
for i in range(1,rows+1):
    print()
    for j in range(1,i+1):
        print("*",end=" ")

rows=int(input("enter the rows: "))
space=rows-1
for i in range(rows):
    for j in range(space):
        print(end=" ")
    space-=1    
    for k in range(1,i):
        print("*" ,end=" ")
        
