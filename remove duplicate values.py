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


##count vowels in string:
a=input("enter your string")
count=0
for  i in a:
    if i  in "aeiouAEIOU":
       count+=1
print(count)


## count vowels in list:
a=int(input("enter the count for how many time do you want enter the string: "))
values=[]
vowels_value=[]
for i in range(a):
    value=input("enter the string value: ")
    values.append(value)
##print(values)
for i in values:
    for j in i:
        if j in "aeiouAEIOU":
            vowels_value.append(i)
            
print("vowel words",list(set(vowels_value)))            
        





    
