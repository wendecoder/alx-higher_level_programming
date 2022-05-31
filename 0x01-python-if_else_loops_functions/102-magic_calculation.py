#!/usr/bin/python3
def magic_calculation(X, Y, Z):
    if X < Y:
        return Z
    elif Z > Y:
        return X + Y
    return (X * Y) - Z
