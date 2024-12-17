a=["apple","banana","orange"]
hw=a[0]
for i in a:
    if len(hw)<len(i):
        hw=i
print(hw)

#-------------------------------
string=input().split()
res=""
for val in string:
   if len(val) > len(res):
        res+=val
print(res)



