#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        line = ''
        for i in range(x):
            line += str(my_list[i])
        print(line, '\n')

    except IndexError:
        print("x should be integer and less or equal to list length")
        continue
    return x
