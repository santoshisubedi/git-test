while True:
	a = float(input('first number:'))
	b = float(input('second number:'))

	try:
		result = a/b
		print('result = {}'.format(result))
	except ZeroDivisionError:
		print('error:Division by Zero')
	try_again = input('\nTry Again (Y/N)?')
	# if the user doesn't want to try again exit the loop.
	if try_again.upper() != 'Y':
		break
	print()
	#program will exit finally.
print('Good Bye!')