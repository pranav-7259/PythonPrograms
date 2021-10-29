# Function Overloading test

def add(a, b):
    return a + b


def add(a, b, c):
    return a + b + c


add(10, 20)
add(10, 20, 30)


# Error as Python does not support overloading

# Resolution

def add(a, b):
    return a + b


add2 = add


def add(a, b, c):
    return a + b + c


add(10, 20, 30)
add2(40, 50)
