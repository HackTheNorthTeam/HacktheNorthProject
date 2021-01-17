class queue:

    def __init__(self, teachers = [], students = []):
        self.teachers = teachers
        self.students = students
        self.line = {}

    def showPairs(self):
        print(self.line)

    def getStudentLength(self):
        return len(self.students)

    def addtoStudentQueue(self, student):
        self.students.append(student)

    def addtoTeacherQueue(self, teacher):
        self.teachers.append(teacher)
    
    def pairTeachersStudents(self):
        for n in range(len(self.teachers)):
            self.line[self.teachers[n]] = self.students[n]
        for n in range(len(self.teachers)):
            self.students.remove(self.students[0])

    def setPair(self, index):
        self.line[index] = self.students[0]
        self.students.remove(self.students[0])

MATH = queue(['teacher 1', 'teacher 2', 'teacher 3'], ['student 1', 'student 2' , 'student 3', 'student 4', 'student 5', 'student 6'])
MATH.pairTeachersStudents()
print(MATH.showPairs())
MATH.setPair('teacher 1')
print(MATH.showPairs())
