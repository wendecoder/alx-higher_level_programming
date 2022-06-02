#!/usr/bin/python3
import sys

if __name__ == "__main__":
    inputs = len(sys.argv) - 1
    inf_add = 0
    for i in range(1, inputs + 1):
        inf_add += int(sys.argv[i])
    print(inf_add)
