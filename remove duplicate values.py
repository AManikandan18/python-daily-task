a=[1,2,3,4,5,1,2,3]
b=set(a)
print(b)

#another way:
a=["mani","psh","asfaak","asfaak"]
b=list(dict.fromkeys(a))
print(b)

##another way:
real_val=[]
for val in a:
    if val not in real_val:
        real_val.append(val)
    else:
        print("this is black goat",val)
print(real_val)
##in comprehension:
r_v=[]
[r_v.append(val) for val in a if val not in r_v]
print(r_v)



##factorial
a=int(input("enter the number: "))
fact=1
for i in range(2,a+1):
    fact=fact*i
    print(fact)


## fibonacci series:
f=int(input("enter the number: "))
a=0
b=1
for i in range(1,f+1):
    c=a+b
    print("the fibonacci value is :",c)
    a=b
    b=c

    


           
        





    
