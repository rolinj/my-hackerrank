class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super(Student, self).__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        average_grade = sum(self.scores) / len(self.scores)
        
        if 101 > average_grade > 89:
            return "O"
        elif 90 > average_grade > 79:
            return "E"
        elif 80 > average_grade > 69:
            return "A"
        elif 70 > average_grade > 54:
            return "P"
        elif 55 > average_grade > 39:
            return "D"
        else:
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