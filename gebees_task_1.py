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
##
####example 2:
##compuuter


x=input()
array=[]
array2=["a","e","i","o","u"]
for i in range(len(x)):
    array.append(x[i])
for k in range(len(array)-1):
    if array[k] in array2:
        if array[k+1] == array[k]:
            break;
        else:
            array.remove(array[k])
print(''.join(array))


