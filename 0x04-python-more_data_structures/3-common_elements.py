#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_elem = ""
    for q, v in zip(set_1, set_2):
        if q == v:
            common_elem = q
    return common_elem
