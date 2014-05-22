#!/usr/bin/env python

# __copyright__ = Brandon Jackson
# __license__ = GPL v2
# This script evaluates passwords.

'''
ts = too short
nu = needs uppercase
nl = needs lowercase
nn = needs number
'''

import getpass, string

def testPassword():
    password_ts, password_nu, password_nl, password_nn = True, True, True, True
    conditions_met = 0
    conditions_message = ''

    password = getpass.getpass('What\'s the password that you want to test?')

    if len(password) > 6:
        conditions_met += 1
        password_too_short = False

    for char in password:
        if char in string.ascii_uppercase:
            conditions_met += 1
            password_needs_uppercase = False

    if char in string.ascii_lowercase:
            conditions_met += 1
            password_needs_lowercase = False

    if char in string.digits:
            conditions_met += 1
            password_needs_number = False

    if conditions_met == 0: conditions_message = 'Your password is very weak.'
    if conditions_met == 1: conditions_message = 'Your password is weak.'
    if conditions_met == 2: conditions_message = 'Your password is average.'
    if conditions_met == 3: conditions_message = 'Your password is awesome.'

    print(conditions_message)

    if any((password_ts, password_nu, password_nl, password_nn)):
        print('\nYou can improve your password by...')
        if password_nl: print('    -using lowercase letters.')
        if password_nu: print('    -using uppercase letters.')
        if password_ts: print('    -using more characters.')
        if password_nn: print('    -using numbers.')

if __name__ == '__main__':
    testPassword()
