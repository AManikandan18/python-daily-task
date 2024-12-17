####1
##a=int(input("enter the first value: "))
##b=int(input("enter the second value: "))
##print(a+b)
##
####2
##a=int(input("enter the first value: "))
##if a%2==0:
##    print("the value",a,"is even")
##
####3    
##a=int(input("enter the first value: "))
##fact=1
##for i in range(1,a):
##    fact*=i
##print("the given number factorial is:",fact)
##
####4
##a=int(input("enter the first value: "))
##b=int(input("enter the second value: "))
##c=int(input("enter the three value: "))
##if a>b and a>c:
##    print("the value",a,"is highest")
##elif b>a and b>c:
##    print("the value",b,"is highest")
##else:
##    print("the value",c,"is greater")
##
####5
##for i in range(20):
##    if i%2==0:
##        print("the even number is",i)
##
##    
####6
##count1=0    
##for i in range(5):
##    count1+=i
##print("the sum value is :",count1)
##
####7
##a="amma"
##if a==a[::-1]:
##    print("palindrome")
##else:
##    print("not a palindrome")
##
####8
##a="mani"
##
##count=0
##for i in a:
##    if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
##        count+=1
##print("the total vowels are",count)
##
####9
##a=[1,2,3,4,5]
##rev=[]
##for i in str(a):
##    rev+=i
##print("the reverse value is :",list(rev))
##
####10    
##a=[1,2,3,4,4,3]
##print(set(a))
##print(dict.fromkeys(a))
##
##
##
####11
##a=int(input("enter the first value: "))
##for i in range(len(a)):
##    if a%i==0:
##        pass
##    else:
##        print("prime")
##
####12        
##a="mani"
##print(a.uppercase())
##
####13
##
##
####14
##a=[1,2,3,4,5]
##print("the maximum value is",max(a))
##
####15
##a=int(input("enter the first value: "))
##print("the square root is:",a**0.5)
##
####16
##
##
####17
##a=int(input("enter the first value: "))
##print(pow(a))
##
####18
##
####19
##
####20
##inp=int(input("enter the first value: "))
##a=10
##a=0
##b=1
##for i in range(inp):
##    print(a)
##    print(b)
##    c=a+b
##    print(c)
##    a=b
##    b=c
##    
####21

a="mani hello"
b=a.split()
print(b)
for i in b:
    for j in range(1,b+1):
        c=len(a[i])<len(a[j])
        print(c)
