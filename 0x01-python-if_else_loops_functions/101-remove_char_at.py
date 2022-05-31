#!/usr/bin/python3
def remove_char_at(str, n):
    j = 0
    edited_str = ""
    while j != len(str):
        if j == n:
            pass
        else:
            edited_str += str[j]
        j += 1
    return edited_str
