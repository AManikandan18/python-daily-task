##a="mani"
# for i in range(len(a)):
#     if ord(a[i])>=97 or ord(a[i])<=122:
#         b=chr(ord(a[i])-32)

# # what is the differents between step over and step in and step out:
# def multiply(a, b): 
#     result = a * b  # Line 2
#     return result   # Line 3

# def add(a, b):
#     result = a + b  # Line 6
#     return result   # Line 7

# def main():
#     x = 5           # Line 10
#     y = 10          # Line 11
#     z = add(x, y)   # Line 12
#     w = multiply(x, y)  # Line 13
#     print(w)        # Line 14

# main()              # Line 16


# Merge Sort:
def mergesort(a):
    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]

        
        mergesort(L)
        mergesort(R)

        a.clear()
        while len(L)>0 and len(R)>0:
            if L[0] <= R[0]:
                a.append(L[0])
                L.pop(0)
            else:
                a.append(R[0])
                R.pop(0)
            

        for i in L:
            a.append(i)
        for i in R:
            a.append(i)

a = [1,2,6,4,0]
mergesort(a)
print(a)



# bobble sort:

# a=[5,4,3,2,78,3,10,1]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]<a[j]:
#             print(a)
#             a[i],a[j]=a[j],a[i]
# print(a)

# a=[2,3,1,4,5]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# Selection Sort
# a=[5,4,3,2,1]
# b=0
# accending=[]
# for i in range(len(a)):
#     temp=a[b]
#     b+=1
#     for j in a:
#         if temp < j:
#             accending.append(temp)
#     print(temp)    
# print("the accending value is",accending)    
