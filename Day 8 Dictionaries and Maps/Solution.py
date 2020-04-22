#Question Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
dicti = dict()

for _ in range(int(input())):
        name, number = input().split(" ")
        dicti[str(name)] = int(number)
      
condition = True
store = []

for _ in range(len(dicti)):
        name = input()
        if name in list(map(str, dicti.keys())):
                store.append(name)
        if name not in list(map(str, dicti.keys())):
                store.append("Not found")
        
for x in store:
        if x == "Not found":
                print(x)
        else:
                print(x + "=" + str(dicti[x]))


