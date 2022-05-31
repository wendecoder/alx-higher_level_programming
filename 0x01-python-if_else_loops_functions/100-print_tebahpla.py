#!/usr/bin/python3
new_Str = ""
j = 122
while j != 96:
    if j % 2 != 0:
        new_Str += chr(j - 32)
    else:
        new_Str += chr(j)
    j -= 1
print("{}".format(new_Str), end="")
