a=1
if a%2==0:
    print("even number")
else:
    print("odd number")


##if condition:
    
##list comprehention:
list_2=[print("even number") if(a%2==0) else print("odd number")]

##set:
set_2={print("even number") if(a%2==0) else print("odd number")}

##for loop:

##list
list2=[i for i in range(1,10) if(i%2==0)]
print("even number is :",list2)

##set
set2=[x for x in range(1,10) if(x%2==0)]
print("even number is: ",set2)
