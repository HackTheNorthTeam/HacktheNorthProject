class queue:
    identifier = None
    teachers = None
    students = None

    line = None

    def __init__(self, identifier, teachers, students):
        self.identifier = identifier
        self.teachers = teachers
        self.students = students

    line = {}

    def pairTeachersStudents(self):
        for n in range(len(self.teachers)):
            self.line[self.teachers[n]] = self.students[n]

        for n in range(len(self.teachers)):
            self.students.remove(self.students[0])

    def removePair(self, index):
        self.line[index] = self.students[0]