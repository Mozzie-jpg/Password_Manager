#!/usr/bin/env python3

"""
More Features will be added in the future.
"""

import os
import hashlib

home_dir = os.getenv("HOME")
pass_man_write = open(home_dir + '/.pass_man', 'a')
pass_man_read = open(home_dir + '/.pass_man', 'r')

def menu():
    print (
        '1. Create new set\n'
        '2. Show all sets\n'
        '3. Exit'
    )

    mode = input('')

    if mode == '1':
        new_set()

    if mode == '2':
        show_sets()

    if mode == '3':
        Quit()

def new_set():

    global pass_man_write

    username = input('username: ')
    password = input('password: ')

    pass_encoded = hashlib.sha512(str.encode(password))
    pass_use = (pass_encoded.hexdigest())


    pass_man_write.write('%s : %s\n' % (username, pass_use))

    pass_man_write = open(home_dir + '/.pass_man', 'a')
    pass_man_read = open(home_dir + '/.pass_man', 'r')

def show_sets():

    global pass_man_read
    print ()
    pass_man_write = open(home_dir + '/.pass_man', 'a')
    pass_man_read = open(home_dir + '/.pass_man', 'r')
    print(pass_man_read.read())

def Quit():
    return False

while menu() == True:
    menu()
