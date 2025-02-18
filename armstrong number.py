#armastrong 

##num=int(input("enter the number: "))
##n=len(str(num))
##sum=0
##temp=num
##while temp>0:
##    digit=temp%10
##    sum=sum+(digit**n)
##    temp=temp//10
##if(num==sum):
##    print("yes,your given number",num," is armstrong")
##else:
##    print("given number is not an armstrong")

#get input in armstrong:

    
num1=int(input("enter start the number: "))
num2=int(input("enter start the number: "))
n=len(str(num1))
sum=0
temp=num1
if temp<=num2:
    while temp>0:
        digit=temp%10
        sum=sum+(digit**n)
        temp=temp//10
        temp+=1
        print(num1)
if num1==sum:
    print("yes,your given number",num," is armstrong")
else:
    print("given number is not an armstrong")

"""
num1=int(input("enter your starting point: "))
n=len(str(num1))
sum=0
temp=num1
while temp>0:
    digit=temp%10
    sum=sum+(digit**n)
    temp=temp//10
if(num1==sum):
    print("armstrong number")
else:
    print("not an armstrong")"""
