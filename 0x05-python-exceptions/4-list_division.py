#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lists = [0] * list_length
    for i in range(list_length):
        try:
            if not isinstance(my_list_1[i], (int, float))
            or not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                lists[i] = 0
            else:
                lists[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            lists[i] = 0
        except IndexError:
            print("out of range")
            lists[i] = 0
    return lists
