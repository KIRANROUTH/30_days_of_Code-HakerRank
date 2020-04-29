#Question Link: https://www.hackerrank.com/challenges/30-sorting/problem

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap = 0
for x in range(len(a) - 1):
    for y in range(x, len(a)):
        val1 = a[x]
        val2 = a[y]
        if val1 > val2:
            a[x] = val2
            a[y] = val1
            swap += 1
print("Array is sorted in {} swaps.".format(swap))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
