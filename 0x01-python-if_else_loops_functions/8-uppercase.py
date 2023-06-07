#!/usr/bin/python3
def uppercase(str):
    uppercase_string = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        uppercase_string += uppercase_char
    print("{}".format(uppercase_string))
