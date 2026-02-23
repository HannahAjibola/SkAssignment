import unittest

from Students import Students
class StudentsTest:

    def __init__(self):
            self.student = []
    def student_is_created(self,name, user_name, age, courses,gender,state):
        self.student.append(Students(name,user_name,age,courses,gender,state))
        assert

    def update_student_student_name(self, user_name, new_name):
        for students in  self.student:
            if students.get_name() == user_name:
                students.set_name(new_name)


if __name__ == '__main__':
    unittest.main()
