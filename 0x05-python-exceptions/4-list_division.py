#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    idx, result = 0, 0
    new_list = []
    while idx < list_length:
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
            idx += 1
    return new_list
