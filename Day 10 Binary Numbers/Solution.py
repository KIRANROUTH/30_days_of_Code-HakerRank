#Question Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem

n = int(input())

bina = str(bin(n))
val = bina[2:]
List = val.split("0")
print(len(max(List)))
