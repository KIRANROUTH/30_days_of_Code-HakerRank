#Question Link: https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    maximumDifference = 0
    newdif = 0
    def computeDifference(self):
        Difference.maximumDifference = 0
        for ele in range(len(self.__elements) - 1):
                for ele_ in range(ele + 1, len(self.__elements) - 1):
                    newdif = abs(self.__elements[ele] - self.__elements[ele_ + 1])
                    if newdif > Difference.maximumDifference:
                        Difference.maximumDifference = newdif


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
