favSnacks = ["chips" ,"gummies", "reeses", "chocolate", "cinnamon rolls"]
favSnacks.append("pretzels")
favSnacks.sort()
for snack in favSnacks:
    print(snack)

myColleges = ("USC", "UCLA", "Hawaii", "UC Berkley", "Tuskegee")
for College in myColleges:
    print(College)

numberGrade = {33, 66, 22, 99, 30}
for grade in numberGrade:
    print(grade)


carAttribute = { "Brand": "Mercedez-Benz",
                "Model": "S-Class",
                "Year": 2023,
                "Engine":"inline-6 turbocharged",
                "WheelSize": "19in"}
carAttribute["color"] = "blue"
for attribute in carAttribute:
    print(carAttribute.get(attribute))