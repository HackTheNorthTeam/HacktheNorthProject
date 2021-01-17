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