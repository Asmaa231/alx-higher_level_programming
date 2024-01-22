#!/usr/bin/python3
def max_integer(my_list=[]):
    if len (my_list) > 1:
        return None
    my_list_cp = my_list.cp()
    my_list_cp.sort()
    return  my_list_cp[-1]
