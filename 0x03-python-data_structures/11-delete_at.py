#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        listDelete = my_list
        del listDelete[idx]
        return listDelete
