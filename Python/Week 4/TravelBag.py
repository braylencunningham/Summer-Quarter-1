bedroom = ["Shirt", "Shorts", "Shoes", "Socks"]

travelBag = []

print("Pack your bags")
print("Enter the index of an item you'd like to move from your room to your bag. ")
print("Type '100' when you are done packing")
print("Your Bedroom Items")
for item in bedroom:
    print(item)

item = int(input("Item Index: "))

while item != 100:
    travelBag.append(bedroom[item])
    bedroom.remove(bedroom[item])
    print("\nYour Bedroom:")
    print(bedroom)
    print("\nYour Travel Bag:")
    print(travelBag)
    item = int(input("Item Index: "))

    