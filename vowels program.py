##count vowels in string:
a=input("enter your string")
count=0
for i in a:
    if i  in "aeiouAEIOU":
       count+=1
print(count)


## print vowels in list correct program:
a=int(input("enter the count for how many time do you want enter the string: "))
values=[]
vowels_value=[]
Vowels="aeiouAEIOU"
for i in range(a):
    value=input("enter the string value: ")
    values.append(value)
for i in values:
    for j in i:
        if str(j) in Vowels:
            vowels_value.append(i)

print("vowel words",list(set(vowels_value))) 
