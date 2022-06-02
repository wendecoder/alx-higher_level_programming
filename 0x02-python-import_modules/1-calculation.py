#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, div, mul
    """
    importing modules

    """
    
    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(10, 5, add(a, b)))
    print("{:d} - {:d} = {:d}".format(10, 5, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(10, 5, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(10, 5, div(a, b)))
