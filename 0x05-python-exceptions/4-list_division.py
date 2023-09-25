#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_lst = []
    for i in range(0, list_length):
        try:
            rslt = my_list_1[i] / my_list_2[i]
        except TypeError:
            rslt = 0
            print("wrong type")
        except ZeroDivisionError:
            rslt = 0
            print("division by 0")
        except IndexError:
            rslt = 0
            print("out of range")
        finally:
            new_lst.append(rslt)
    return new_lst
