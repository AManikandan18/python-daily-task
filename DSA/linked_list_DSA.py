
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





# class Node:
#     def __init__(self,data):
        # self.data=data
#         self.pointer=None
    

#     def add(self,value):
#         self.pointer=value
#         print(self.pointer)
#         # print(self.pointer)
#         # return self.pointer
    
#     def display(self):
#         # if self.pointer is not None:
#         # if self.pointer:
#         while(self.pointer is not None):
#             print(self.data)
#             self.data=self.pointer  
#             break
    # def display(self):
    #     # if self.pointer is not None:
    #     if self.pointer:
    #         print("empty")
    #     else:
    #         while(self.data is not None):
    #             print(self.data)
    #             self.data=self.pointer  

    # def insert(self,index,value):
    #     self.linked_list.insert(index,value)
    #     print(self.linked_list)
    # def delete(self,value):
    #     rmv=self.linked_list.remove(value)
    #     print(rmv)
    # def isempty(self):
    #     if self.linked_list:
    #         return False
    #     else:
    #         return True    

# head=Node(5)
# head2=Node(6)
# head3=Node(7)
# # head.add(7)
# # head.add(8)
# print("the ",head2)
# head.add(head2)
# head.add(head3)
# # print(head3)
# head.display()


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

linked=LinkedList()
linked.add(5)                
linked.add(6)                
linked.add(7) 
linked.add(8)

linked.display()