#return the missing value in the list:
a=[1,3,5,7,9]
missing_value=[]
for i in range(a[0],a[-1]):
    if i not in a:
        missing_value.append(i)
print(missing_value)        
