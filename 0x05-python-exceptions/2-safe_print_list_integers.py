#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    nb_digit = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            nb_digit += 1
        except (TypeError, ValueError):
            pass
    print()
    return nb_digit
