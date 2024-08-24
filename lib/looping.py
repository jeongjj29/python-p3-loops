#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    if i == 0:
        print("Happy New Year!")
    pass

def square_integers(int_list):
    squared_integer_list = [int * int for int in int_list]
    return squared_integer_list
    pass

def fizzbuzz():
    for i in range(100):
        if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
            print("FizzBuzz")
        elif (i + 1)% 3 == 0:
            print("Fizz")
        elif (i + 1)% 5 == 0:
            print("Buzz")
        else:
            print(i + 1)
    pass
