#swap value
a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)
#swap the value without use the third variable:  
a=10
b=20
b=a+b
a=b-a
b=b-a
print(a)
print(b)
