#No of digits in a string

s = input("Enter a string: ")

for c in s:
    if c.isdigit():
        print(c,end = "")
    else:
        continue
