##count vowels in string:
a=input("enter your string")
count=0
for i in a:
    if i  in "aeiouAEIOU":
       count+=1
print(count)


## print vowels in list:
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
