# Print even numbers first then odd numbers


even = []
odd = []

i = 0
while i < 10:
    num = int(input("Enter a number: "))
    i += 1
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

for e in even:
    print(e, end=" ")

for o in odd:
    print(o, end=" ")
