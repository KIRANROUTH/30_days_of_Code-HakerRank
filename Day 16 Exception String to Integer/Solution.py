#Question Link: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

try:
    S = input().strip()
    print(int(S))
except Exception as e:
    print("You got: ")
