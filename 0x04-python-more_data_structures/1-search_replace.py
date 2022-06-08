#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced_list = []
    for i in range(len(my_list)):
        if my_list[i] != search:
            replaced_list.append(my_list[i])
        else:
            replaced_list.append(replace)
    return replaced_list
