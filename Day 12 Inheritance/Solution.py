#Question Link: https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    average = 0
    def __init__(own, first, last, id, scores):
        super().__init__(first, last, id)
        own.scores = list(map(int, scores))

    
    
    def calculate(own):
        Student.average = sum(own.scores)/len(own.scores)
        if Student.average <= 100 and Student.average >= 90:
            return "O"
        if Student.average < 90 and Student.average >= 80:
            return "E"
        if Student.average < 80 and Student.average >= 70:
            return "A"
        if Student.average < 70 and Student.average >= 55:
            return "P"
        if Student.average < 55 and Student.average >= 40:
            return "D"
        if Student.average < 40:
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
