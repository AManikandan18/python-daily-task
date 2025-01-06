#swap value with using third variable:
a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)
print("second method")

#swap the value without use the third variable:  
a=10
b=20
b=a+b
a=b-a
b=b-a
print(a)
print(b)
print("third method")

#next way
a=10
b=20
a,b=b,a
print(a)
print(b)
