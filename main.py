import random

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '!"%&@/();:,-.'
password = ''

def asklength():
	password_length = int(input('How long do you want the password to be? (8-20 characters) \n'))
	if password_length > 7 and password_length < 21:
		return password_length
	else:
		print('Please enter a valid number between 8 and 20.')
		return asklength()

def addlower():
	global password
	global letters
	password += random.choice(letters)

def addupper():
	global password
	global letters
	password += random.choice(letters).upper()

def addnum():
	global password
	global numbers
	password += random.choice(numbers)

def addsymb():
	global password
	global symbols
	password += random.choice(symbols)

password_functions = [addlower, addupper, addnum, addsymb]

def main():
	global password
	password_length = asklength()
	for i in range(password_length):
		random.choice(password_functions)()
	return password

print(main())





