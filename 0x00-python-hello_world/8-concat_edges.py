#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split(", ")[2][:28] + str[107:112] +  str[:6]
print(str)
