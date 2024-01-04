#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    nb_digit = 0
    line = ''
    for i in range(x):
        try:
            line += str(my_list[i])
            nb_digit += 1
        except (TypeError, ValueError):
            pass
    print(line)
    return nb_digit
