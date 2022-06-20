#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    newList = []
    index = 0
    if list_length <= 0:
        print("out of range")
        return newList
    while index < list_length:
        try:
            newList.append(my_list_1[index] / my_list_2[index])
        except ZeroDivisionError:
            print("division by 0")
            newList.append(0)
        except TypeError:
            print("wrong type")
            newList.append(0)
        except IndexError:
            print("out of range")
            newList.append(0)
        finally:
            index += 1
    return newList
