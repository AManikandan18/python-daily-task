##sorting without using methods:
##in accending to decending:

in_list=[3,2,1,-5,4]

out_list=[]

while in_list:
    min_val=in_list[0]
    for value in in_list:
        if min_val>value:
            min_val=value
    out_list.append(min_val)
    in_list.remove(min_val)
print(out_list)     

##in decending to accending:

out_list=[]

while in_list:
    min_val=in_list[0]
    for value in in_list:
        if min_val < value:
            min_val=value
    out_list.append(min_val)
    in_list.remove(min_val)
print(out_list)
