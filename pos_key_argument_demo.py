def func(*pos, **key):
    for k, v in key.items():
        print(pos, k, v)


func(10, 20, fname='Pranav', lname='Shekhar')
