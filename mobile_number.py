#Finding from string if it is a 10 digit mobile number or not

s = input("Enter a string: ")

count = 0
for c in s:
    if c.isdigit():
        count += 1
    else:
        print("It is not mobile number")
        break

if count == 10 and count == len(s):
    print("It is mobile number")

