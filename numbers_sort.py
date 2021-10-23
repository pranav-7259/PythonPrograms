#Sorting the numbers

l = []
while True:
    n = int(input("Enter a number [-1 to end]: "))
    if n == -1:
        break
    else:
        l.append(n)


for num in sorted(l):
    print(num, end=" ")
