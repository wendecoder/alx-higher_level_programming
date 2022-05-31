#!/usr/bin/python3
for j in range(0, 10):
    for k in range(0, 10):
        if j < k:
            if j == 8 and k == 9:
                print("89")
                break
            print("{}{},".format(j, k), end=' ')
