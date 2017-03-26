a = float(input('first number:'))
b = float(input('second number:'))

try:
	result = a/b
	print('result',result)
except ZeroDivisionError:
	print('error:Division by Zero')