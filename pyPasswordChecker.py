#!/usr/bin/env python

# __copyright__ = Brandon Jackson
# __license__ = GPL v2
# This script evaluates passwords.

import getpass

def testPassword():
	password_too_short, password_needs_uppercase, password_needs_lowercase, password_needs_number = True, True, True, True
	conditions_met = 0
	conditions_message = ''

	password = getpass.getpass('What\'s the password that you want to test?')

	if len(password) > 6:
		conditions_met += 1
		password_too_short = False

	if password.isupper():
		conditions_met += 1
		password_needs_uppercase = False

	elif password.islower():
		conditions_met += 1
		password_needs_lowercase = False

	elif password.isdigit():
		conditions_met += 1
		password_needs_number = False

	if conditions_met == 0: conditions_message = 'Your password is very weak.'
	if conditions_met == 1: conditions_message = 'Your password is weak.'
	if conditions_met == 2: conditions_message = 'Your password is average.'
	if conditions_met == 3: conditions_message = 'Your password is awesome.'

	print(conditions_message)

	if any((password_too_short, password_needs_uppercase, password_needs_lowercase, password_needs_number)):
		print('')
		print('You can improve your password by...')
		if password_needs_lowercase: print('    -using lowercase letters.')
		if password_needs_uppercase: print('    -using uppercase letters.')
		if password_too_short: print('    -using more characters.')
		if password_needs_number: print('    -using numbers.')

if __name__ == '__main__':
	testPassword()
