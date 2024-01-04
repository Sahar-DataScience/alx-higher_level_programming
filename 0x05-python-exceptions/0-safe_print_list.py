#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nb_digit = 0
    try:
        line = ''
        for i in range(x):
            print(my_list[i], end='')
            nb_digit += 1

    except IndexError:
        pass
    return nb_digit
