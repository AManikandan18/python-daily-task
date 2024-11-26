a=int(input("Enter you A value: "))
b=int(input("Enter you B value: "))
c=int(input("Enter you C value: "))
if a>c:
    if a>b:
        print("The value A",a,"is greater than b and c")
    else:
        print("The value B",b,"is greater than a and c")
else:
    print("The value C",c,"is greater than a and b")


##another way:

if a>b and a>c:
    print("The value A",a,"is greater than b and c")
elif b>a and b>c:
    print("The value B",b,"is greater than a and c")
else:
    print("The value C",c,"is greater than a and b")
