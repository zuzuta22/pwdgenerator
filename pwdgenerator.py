# coding: utf-8

import random
import string

# Words in the exlusive_list are not included in password
exclusive_list = ["0", "o", "O", "1", "l", 0, 1, "q", 9, "9",]

# Worls in symbols_list are included in password
symbols = ["@", "#", "%", "&", "?",]

def create_random_string(elems, len = 4):
    r_string = ""
    while len:
        element = random.choice(elems)
        if element in exclusive_list:
            continue
        else:
            r_string += element
            len -= 1
    return r_string

def check_complexity(pwd, symbols):
    counter = 0
    chars = list(pwd)
    for c in chars:
        if c in symbols:
            counter += 1
    if counter > 2:
        return True
    else:
        return False

def create_pwd():
    elements = string.lowercase + string.uppercase + \
            string.digits + "".join(symbols)
    password = ''
    while not check_complexity(password, symbols):
        password = create_random_string(elements, 8)

    return password

def main():
    print create_pwd()

if __name__ == '__main__':
    main()
