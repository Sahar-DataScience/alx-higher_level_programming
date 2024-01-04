#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nb_digit = 0
    try:
        line = ''
        for i in range(x):
            line += str(my_list[i])
            nb_digit += 1

    except IndexError:
        pass
    print(line)
    return nb_digit
