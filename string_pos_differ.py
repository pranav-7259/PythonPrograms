# Print pos of character where strings differ

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

i = 0
pos = -1

while i < min(len(s1), len(s2)):
    if s1[i] != s2[i]:
        pos = i
        break
    i+=1

if len(s1) == len(s2) and pos == -1:
    print("Strings are same")
elif pos == -1 and len(s1) != len(s2):
    print(f"Strings differ at position {min(len(s1), len(s2)) + 1}")
else:
    print(f"The position at which they differ is {pos}")
