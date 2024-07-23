name=["mani","paramesh","asfaak"]
age=[21,23,22]
b=zip(name,age)
for i in b:
    print(i)
##
print()
for i in zip(name,age):
    print(i)


##
k={}    
for i,j in name,age:
    k[i]=zip(j)
print(k)
