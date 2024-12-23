
# Single Linked List:

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.pointer=None

# head=Node(2)
# node2=Node(3)
# node3=Node(4)
# node4=Node(5)
# node5=Node(6)
# node6=Node(7)


# head.pointer=node2
# node2.pointer=node3
# node3.pointer=node4
# node4.pointer=node5
# node5.pointer=node6

# # print(head.data)
# # print(head.pointer)

# cur=head

# while(cur is not None):
#     print(cur.data)
#     cur=cur.pointer


# -------------------

class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None

class LinkedList:
    def __init__(self):
        self.head=None        
    def add(self,data):
        NewNode=Node(data)
        if self.head is None:
            self.head=NewNode
        else:
            cur=self.head
            while(cur.pointer is not None):
                cur = cur.pointer
            cur.pointer=NewNode  
    def display(self):
        cur = self.head 
        while(cur is not None):
            print(cur.data,end=" ")                                     
            cur=cur.pointer      

    def remove(self,data) :
        if self.head is not None:
            if self.head.data==data:
                self.head=self.head.pointer
            else:
                cur=self.head
                while(cur.pointer is not None):

linked = LinkedList()
linked.add(5)                
linked.add(6)                
linked.add(7) 
linked.add(8)
linked.add(9)

linked.display()