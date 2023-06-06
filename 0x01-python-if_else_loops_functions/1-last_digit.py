#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_number = str(number)[-1]

if int(last_digit_number) > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit_number))
elif int(last_digit_number) == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit_number))
elif int(last_digit_number) < 6 and last_digit_number != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit_number))
