#Question Link: https://www.hackerrank.com/challenges/30-queues-stacks/problem

import sys
from collections import deque

class Solution:
    # Write your code here
    def __init__(self):
        self.word1 = []
        self.word2 = []

    def pushCharacter(self, letter1):
        self.word1.append(str(letter1))
    
    def enqueueCharacter(self, letter2):
        self.word2.append(str(letter2))
    
    def popCharacter(self):
        return self.word1.pop()

    def dequeueCharacter(self):
        self.word2 = deque(self.word2)
        return self.word2.popleft()


# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
