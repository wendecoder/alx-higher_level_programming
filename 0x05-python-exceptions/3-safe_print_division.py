#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        output = a / b
        print("Inside result: {:.1f}".format(output))
    except:
        output = None
        print("Inside result: {}".format(output))
    finally:
        return output
