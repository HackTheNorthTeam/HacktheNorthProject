class queue:
    identifier = None
    teachers = None
    students = None

    line = None

    def __init__(this, identifier, teachers, students):
        this.identifier = identifier
        this.teachers = teachers
        this.students = students

    line = {}

    def pairTeachersStudents(this):
        for n in range(len(this.teachers)):
            this.line[this.teachers[n]] = this.students[n]

        for n in range(len(this.teachers)):
            this.students.remove(this.students[0])

    def removePair(this, index):
        this.line[index] = this.students[0]