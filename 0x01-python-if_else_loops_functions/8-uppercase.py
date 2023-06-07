#!/usr/bin/python3
def uppercase(str):
    uppercase_string = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        uppercase_string += uppercase_char
    return uppercase_string
