value=[1,2,3,4,5]
n=str(value)
target=8
##for i in range(n):
##    for j in range(i):
##        if value[i]+value[j]==target:
##            print(i)
##            print(j)
##            print(value[j])
##            print(value[i])
a=0
b=0
while value:
    if value[a]+value[b]==target:
        print("hu")
        b+=1
    else:
        print("hello")
        
            
    
