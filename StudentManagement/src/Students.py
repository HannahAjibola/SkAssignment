class Students:
    def __init__(self, name,user_name,age,courses,gender,state):
        self.name = name
        self.user_name = user_name
        self.age = age
        self.courses = courses
        self.gender = gender
        self.state = state

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name