student = {}

studentName = input("Enter your student's name: ")
student["Name"] = studentName

studentAge = input("Enter your student's age:")
student["Age"] = studentAge

studentGrade = input("Enter your student's grade:")
input("Enter your student's hobby; Type done when done: ")

hobbies = []
hobby = input("Enter your student's hobby; Type done when done: ").lower()
hobbies.append(hobby)

while hobby is "done":
    hobby = input("Enter your student's hobby, Type 'done' when done: ").lower()
    hobbies.append(hobby)

student["hobbies"] = hobbies

print(student)
