# Print the largest name based on ASCII

largest = ""

while True:
    name = input("Enter a name: Input ['end']  to end: ")
    if name == "end":
        break

    if name > largest:
        largest = name
    else:
        largest = ""

if largest != "":
    print(f"Largest name is {largest}")
else:
    print("There are no largest name")
