geniuses = ["Braylen", "Kenlon"]

for genius in geniuses:
    print(genius)

answer = input("Do you want me to print the list again? Y/N")
while answer == "Y":
    for genius in geniuses:
        print(geniuses)
    answer = input("Do you want me to print the list again? Y/N")
        

