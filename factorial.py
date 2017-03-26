#program to calculate the factorial of integer n taken from the user input.
def main():
	N = input('enter the number')
	n = int(N)
	print('the factorial of{} is {}'.format(n,fact(n)))
def fact(n):
	while n<1:
		return 1
		return n* fact(n-1)
		main()