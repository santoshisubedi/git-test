#create a list of squares of numbers up to 10
squares = [x**2 for x in range(10)]
print('squares:', squares)

#you can create lists using existing lists.
numbers = [1,2,3,4,5,6,7,8,8,10]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]
print('numbers:', numbers)
print('Even numbers:', even_numbers)
print('odd numbers:',odd_numbers)
