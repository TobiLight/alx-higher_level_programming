#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("{:02d}".format(i), end=", ")
        continue
    if i == 99:
        print("{}".format(i))
        break
    print("{}".format(i), end=", ")
