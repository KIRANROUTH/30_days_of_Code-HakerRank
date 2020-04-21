#Question Link: https://www.hackerrank.com/challenges/30-2d-arrays/problem

matrix = []
for x in range(6):
        List = list(map(int, input().split(" ")))
        matrix.append(List)
val = []
for x in range(len(matrix) - 2):
        for y in range(len(matrix[0]) - 2):
              newval = sum(matrix[x][y:y + 3]) + matrix[x + 1][y + 1] + sum(matrix[x + 2][y:y + 3])
              val.append(int(newval))
print(max(val))
