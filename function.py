#function to print the fibonacci series.
def fib(n):
	a, b = 0, 1
	while a < n:
		print(a)
		(a, b) = (b, a+b)
fib(50)