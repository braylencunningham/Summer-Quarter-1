class StudentProfile:
    
    def __init__(self, name, age, grade, hobbies):
        self.student = {}
        self.student = ["Name"] = name
        self.student = ["Age"] = age
        self.student = ["Grade"] = grade
        self.student = ["Hobbies"] = hobbies



    def SetName(self):
        studentName = input("Enter your student's name: ")
        self.student["Name"] = studentName

    def SetName(self):
        studentAge = input("Enter your student's age:")
        self.student["Age"] = studentAge

    def SetGrade(self):
        studentGrade = input("Enter your student's grade:")
        input("Enter your student's hobby; Type done when done: ")

    def SetHobbies(self):
        hobbies = []
        hobby = input("Enter your student's hobby; Type done when done: ").lower()
        hobbies.append(hobby)

    while hobby is "done":
        SetHobbies.append(hobby)
        hobby = input("Enter your student's hobby, Type 'done' when done: ").lower()
    self.student["Hobbies"] = SetHobbies

    print(self.student)
