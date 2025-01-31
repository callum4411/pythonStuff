class Student:
    def __init__(self, name, age, average):
        self.age = age
        self.name = name
        self.average = average

    def __str__(self):
        return "Name: " + self.name + " Age: " + str(self.age) + " Average: " + str(self.average)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getAverage(self):
        return self.average


class ClassRecord:
    def __init__(self):
        self.record = []
        self.index = 0

    def add_student(self, student):
        if len(self.record) < 13:
            self.record.append(student)

    def print_record(self):
        for Student in self.record:
            print(Student)

    def search_student(self, name):
        found = False
        if found == False:
            for Student in self.record:
                if Student.getName() == name:
                    found = True
                    result = Student
        if found == True:
            return result
        else:
            return "null"

    def get_oldest_student(self):
        oldestAge = 0
        for Student in self.record:
            if Student.getAge() > oldestAge:
                oldestAge = Student.getAge()
                oldest = Student
        return oldest

    def get_class_average(self):
        sum = 0
        nstudents = 0
        for Student in self.record:
            nstudents += 1
            sum = sum + Student.getAverage()
        return sum / nstudents

    def get_highest_average_grade(self):
        heighestGrade = 0
        for Student in self.record:
            if Student.getAverage() > heighestGrade:
                heighestGrade = Student.getAverage()
                heighest = Student
        return heighest

    def get_student_ages(self):
        ages = []
        for Student in self.record:
            ages.append(Student.getAge())
        return ages

    def get_passing_students(self):
        stu = []
        for Student in self.record:
            if Student.getAverage() >= 50:
                stu.append(Student.getName())
        return stu

    def pass_fail_remarks(self):
        state = []
        for Student in self.record:
            if Student.getAverage() >= 50:
                state.append("P")
            else:
                state.append("F")
        return state

    def print_by_age(self, age):
        qualifying = []
        for Student in self.record:
            if Student.getAge() >= age:
                qualifying.append(Student.getName())
        return qualifying

    def group_students(self, start, end):
        result = []
        for x in range(start, (end + 1)):
            result.append(self.record[x])
        return result


if __name__ == "__main__":
    print("testing started")
    cl = ClassRecord()
    s1 = Student("Jack", 18, 4.02)
    print(s1)
    print(s1.getName())
    # done testing student functions
    cl.add_student(s1)
    cl.print_record()
    s2 = Student("Callum", 17, 50)
    cl.add_student(s2)
    cl.print_record()
    print(cl.search_student("Callum"))
    print(cl.get_oldest_student())
    print(str(cl.get_class_average()))
    print(cl.get_highest_average_grade())
    print(cl.get_student_ages())
    print(cl.get_passing_students())
    print(cl.pass_fail_remarks())
    print(cl.print_by_age(18))
    s3 = Student("William", 19, 48)
    cl.add_student(s3)
    s4 = Student("Nick", 16, 60)
    cl.add_student(s4)
    for Student in cl.group_students(0,1):
        print(Student)