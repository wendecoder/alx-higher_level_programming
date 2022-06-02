#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    for a in list:
        if a[0] != '_':
            print("{}".format(a))
