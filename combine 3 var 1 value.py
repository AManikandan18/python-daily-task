##a = ['hii','bye','she']
##b = ['scan','then','morn','horn']
##c = ['1011','2345','5678','9876']
##d=[]
####concodinate=[]
####for i in range(len(a)):
####    e=a[0][i],a[1][i],a[2][i]
####    d.append(e)
######print(d)
####
####for i in d:
####    con=i
####    print(con)
##
##
### Given list of tuples
##tuples_list = [('h', 'b', 's'), ('i', 'y', 'h'), ('i', 'e', 'e')]
##
### Initialize an empty list to store the result
##result = []
##
### Iterate over each tuple in the list
##for tup in tuples_list:
##    # Join the elements of the tuple into a single string
##    concatenated_string = ''.join(tup)
##    # Create a new tuple with the concatenated string and add it to the result list
##    result.append((concatenated_string,))
##
### Print the final result
##print(result)
##
##
##
##
a=["12345","12345","12345","12345","12345"]
ordered=[]
n=len(a)

temp=''

for i in a:
    for j in i:
        temp+=j
print(temp)        

stop=0
while stop<=n-1:

    for i in temp:
        temp1=temp[stop::n]
    print(temp1)
    ordered.append(temp1)
    stop+=1
print(ordered)
















        
