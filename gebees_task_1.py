##vowels="aeiouAUIOU"
##a="cat"
##b=" "
####example 1:
##for i in a:
##    if i not in vowels:
##        b=b+i
##    else:
##        pass
##
##print(b)

##example 2:
vowels="aeiouAUIOU"
a="compuuter"
b=["uuUU"]
c=" "
for i in a:
    if i not in vowels and not in b:
        c=c+i
    else:
        pass
print(c)
