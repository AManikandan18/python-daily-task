##palindrome:
#first way:
a="mani"
rev_value=""
for i in a:
    rev_value=i+rev_value
if a==rev_value:
    print("This is Palindrome")
else:
    print("Not a Palindrome")

##second way:
a=input("enter youe value: ")
if a==a[::-1]:
    print("YES,your word",a,"is palindrome.")
else:
    print("no")
    
