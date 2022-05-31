#!/usr/bin/python3
def uppercase(str):
    j = 0
    capStr = ""
    while j != len(str):
        if ord(str[j]) >= 97 and ord(str[j]) <= 122:
            capStr += chr(ord(str[j]) - 32)
        else:
            capStr += str[j]
        j += 1
    print("{}".format(capStr))
