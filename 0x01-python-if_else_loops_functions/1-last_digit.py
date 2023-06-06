#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    if (last_digit * -1) < 6 and (last_digit * -1) != 0:
        print(f"Last digit of {number} is {last_digit * -1} and is less than",
                f"6 and not 0")
else:
    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and", 
        f"is greater than 5")
    elif last_digit == 0:
        print("Last digit of {} is {} and is 0".format(number, last_digit))
