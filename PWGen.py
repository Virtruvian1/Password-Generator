#!/usr/bin/python
#Password Generator

import random
import time

var = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+|:"?`-=[]\;,'

print "-----Password Generator 2019-----\n"

View = raw_input('View Data (Y or N)? ')

if View == 'Y':
    f= open("PWTracker.txt", "r")
    contents = f.read()
    print("\n" + contents)
else:
    save = raw_input('Save (Y or N)? ')
    PasswordId = raw_input('ID for saved Passwords? ')
    amount = int(input('Number of Passwords? '))
    length = int(input('Password Length? '))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print "\n"
    for p in range(amount):
        password = ' '
        for c in range(length):
            password += random.choice(var)
        if save == 'Y':
            f = open("PWTracker.txt", "a+")
            f.write(PasswordId + '     ' + password + '     ' + 'Created at: ' + timestr + "\n")
            print(password + ' _____saved' + ' _____' + timestr + ' _____' + PasswordId)
        else:
            print(password + ' _____not saved' + ' _____' + timestr)

print "Written by: Zachary Allen"
print "Copyright (C) 2020 Vitruvian"
print "GNU General Public License v3.0"
print "Version 1.0"
