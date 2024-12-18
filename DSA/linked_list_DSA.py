# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.pointer=None
# head=Node(2)
# traversal2=Node(3)
# traversal3=Node(4)
# head.pointer=traversal2
# traversal2=traversal3
# print(head.data) 
# print(head.pointer)

# cur=head
# while cur is not None:
#     print(cur.data)
#     cur=cur.pointer


class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None

head=Node(2)
node2=Node(3)
node3=Node(4)
node4=Node(5)
node5=Node(6)


head.pointer=node2
node2.pointer=node3
node3.pointer=node4
node4.pointer=node5

print(head.data)
# print(head.pointer)

cur=head

while(cur is not None):
    print(cur.data)
    cur=cur.pointer

