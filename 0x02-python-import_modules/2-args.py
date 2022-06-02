#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        print("1:", sys.argv[1])
    else:
        print("{:d} arguments:".format(count))
        for i in range(count):
            print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
