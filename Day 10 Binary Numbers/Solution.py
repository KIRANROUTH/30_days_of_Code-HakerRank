n = int(input())

bina = str(bin(n))
val = bina[2:]
List = val.split("0")
print(len(max(List)))
