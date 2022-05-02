#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lists = my_list.copy()
    if idx < 0:
        return lists
    elif idx > len(my_list):
        return lists
    else:
        for i in range(len(lists)):
            if i == idx:
                lists[i] = element
                return lists
        return my_list
