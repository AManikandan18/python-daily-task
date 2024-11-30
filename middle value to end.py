##print the value middle to end:
a=[1,2,3,4,5,6]
n1=len(a)
n=n1//2
b=[]
for i in range(a[n],a[-1]+1):
    b.append(i)
for i in range(a[0],a[n]):
    b.append(i)
print(b)
