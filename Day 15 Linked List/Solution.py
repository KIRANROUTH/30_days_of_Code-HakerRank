#Question Link: https://www.hackerrank.com/challenges/30-linked-list/problem

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    defnode = 0
    def insert(self,head,data): 
    #Complete this method
        if head == None:
            Solution.defnode = Node(data)
            return Node(data)
        else:
            val = Solution.defnode
            while val.next != None:
                val = val.next
            val.next = Node(data)
            return Solution.defnode
                

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
