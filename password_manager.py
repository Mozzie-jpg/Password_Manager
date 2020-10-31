#!/usr/bin/python3

from cryptography.fernet import Fernet
import os

home_dir = os.getenv("HOME")
file = open(home_dir + '/.key', 'rb')
key = file.read()
file.close()
f = Fernet(key)
pass_man_write = open(home_dir + '/.pass_man', 'a')
pass_man_read = open(home_dir + '/.pass_man', 'r')

def menu():
    print (
        '1. Create new set\n'
        '2. Show all sets\n'
        '3. Exit'
        '\n'
    )

    mode = input('')

    if mode == '1':
        new_set()
        menu()

    if mode == '2':
        show_sets()
        menu()

    if mode == '3':
        Quit()

def new_set():

    global pass_man_write
    global f

    username = input('username: ')
    username_encoded = username.encode()
    username_bytes = bytes(username_encoded)
    user_encrypted = f.encrypt(username_bytes)

    password = input('password: ')
    password_encoded = password.encode()
    password_bytes = bytes(password_encoded)
    pass_encrypted = f.encrypt(password_bytes)

    pass_man_write.write('\n%s\n%s' % (user_encrypted.decode(), pass_encrypted.decode()))

def show_sets():

    global f
    print()

    with open(home_dir + '/.pass_man') as file:
        for fi in file.readlines():
            fi_encoded = fi.encode()
            fi_bytes = bytes(fi_encoded)
            decrypted = f.decrypt(fi_bytes)
            print ('%s' % (decrypted.decode()))

    print ()

def Quit():
    return False

while menu() == True:
    menu()
