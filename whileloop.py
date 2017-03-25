#list and the while loop.
names = ['John Doe', 'Jane Doe', 'Johnny Turk', 'Molly Mormon']
i = 0
total_names = len(names)
print('users')
while i < total_names:
	end = ' and\n' if i == total_names - 2 else '\n'
	print(' - %s' %names[i], end=end)
	i+=1
	