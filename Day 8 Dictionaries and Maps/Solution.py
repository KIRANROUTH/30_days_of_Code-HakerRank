#Question Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
n = int(input())
dicti = dict()

for x in range(n):
    name, number = input().split(" ")
    dicti[name] = number

condition = True
names = []
while condition:
    name = input()
    names.append(name)
    if name == "":
        condition = False
        names.pop()

for x in names:
    if x in list(dicti.keys()):
        print(x + "=" + dicti[x])
    else:
        print("Not found")


