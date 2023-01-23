#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx, count = 0, 0
    while idx < x:
        try:
            print("{:d}".format(my_list[idx]), end="")
            idx += 1
            count += 1
        except (ValueError, TypeError):
            idx += 1
            continue
    print("")
    return count
