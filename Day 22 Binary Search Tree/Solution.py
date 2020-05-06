#Question Link: https://www.hackerrank.com/challenges/30-binary-search-trees/problem
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
        
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root, groot = None, string = None, List = []):
        height = 0
        if groot == None:
            groot = root
        if string == None:
            string = str()
        if root.left != None:
            string += str(root.data) + ","
            List = self.getHeight(root.left, groot, string)
        if root.right != None:
            string += str(root.data) + ","
            List = self.getHeight(root.right, groot, string)
        if root.right == None and root.left == None:
            string += str(root.data)
            List.append(string.split(","))
            for list_ in List:
                a = list_
                for val in a:
                    while a.count(val) > 1:
                        a.remove(val)
        if root.left == groot.left and root.right == groot.right:
            return len(max(List)) - 1
        return List

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
