# def mergesort(a):
#     if 1<len(a):
#         mid=len(a)//2
#         L=a[:mid]
#         R=a[mid:]
#         a.clear()
#         while len(L)>0 and len(R)>0:
#             if L[0]<R[0]:
#                 a.append(L[0])
#                 L.pop(0)
#             else:
#                 a.append(R[0])
#                 R.pop(0)

# a=[5,4,3,2,1]
# mergesort(a)
# print(a)

# a=[5,4,3,2,78,3,10,1]
#bobble sort
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]<a[j]:
#             print(a)
#             a[i],a[j]=a[j],a[i]
# print(a)
a=[5,4,3,2,78,3,10,1]

