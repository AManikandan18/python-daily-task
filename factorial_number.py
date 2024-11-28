##Factorial by using For loop:
##a=int(input("Enter your value: "))
##if a==0 or a<0:
##    print("\"wrong\" enter the valid input: ")
##else:
##    fact=1
##    for i in range(1,a+1):
##        fact*=i
##    print("The Factorial number is: ",fact)    

##While loop:
a=int(input("Enter the value: "))
if a==0 or a<0:
    print("\"wrong\" enter the valid input: ")
else:
    fact=1
    while(a>0):
        fact*=a
        a-=1
    print("The Factorial number is: ",fact)    
