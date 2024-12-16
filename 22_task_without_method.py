####1
##a=10
##b=2
##print(a+b)
##
####2
##a=10
##if a%2==0:
##    print("even")
##else:
##    print("not a even")
##
####3
##a=5
##fact=1
##for i in range(5):
##    fact=fact*i
##print(fact)
##
####4
##a=10
##b=20
##c=30
##if a>b and a>c:
##    print(a)
##elif b>a and b>c:
##    print(b)
##else:
##    print(c)
##
####5
##for i in range(20):
##    if i%2==0:
##        print(i)
####6
##a=0
##for i in range(5):
##    a+=i
##print(a)
##
####7
##a="amma"
##real=""
##for i in a:
##    real=i+real
##if a==real:
##    print("alindrome")
##
####8
##a="mani"
##cnt=0
##for i in a:
##    if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
##        cnt+=1
##print(cnt)
##
####9
##a=["1","2","3","4","5"]
##b=""
##for i in a:
##    b=i+b
##print(list(b))    
##
####10
##a=["mani","naveen","mani"]
##for i in a:
##    if i in a:
##        a.remove(i)
##    print(a)
##
####11    
##a=5
##for i in a:
##    if a%i==0:
##        print("not a prime")
##    else:
##        print("prime")
####12
##a=["mani"]
##b=[]
##for i in range(len(a)):
##    if ord(a[i])>97 or ord(a[i]<122):
##        print(chr(ord(i)))
##
####13
####14
##a=[1,2,3,4,5]
##for i in range(len(a)):
##    for j in range(len(a)):
##        if a[i]<a[j]:
##            print(i)
##
####15     
##a=5
##print(a**0.5)
##
####16
##a=input()
##b=input()
##if a==b:
##    print("anagrams")
##else:
##    print("not anagrams")
##
####17    
##a=int(input())
##print(a*a)
##
####18
##a=["rain rain come again"]
##a.split(" ")
##for i in a:
##    
##
##
##
####19
##a=["mani","naveen","mohan"]
##b=["kumar","naveen","nazar"]
##for i in a:
##    for j in a:
##        if a==j:
##            print(i,"is common element")
##
####20
##a=0
##b=1
##for i in range(20):
##    print(a)
##    print(b)
##    c=a+b
##    a=b
##    b=c
##    
####21
##a=2000
##if a%400==0 and a%4==0:
##    print("leap year")
##elif a%4==0 or a%100!=0:
##    print("leap year")
##else:
##    print("not a leap year")

##22    
a=int(input("enter number of table: "))
b=int(input("how many time you run table: "))
for i in range(1,b+1):
    print(i,"*",a,"=",i*a)
    
    
