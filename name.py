names = ['john Doe','jane Doe','johny truk']
#change the first name in the last
names[0] = 'foo bar'
print ( 'names now :', names)
#Append some more names
names.append('Molly Mormon')
names.append('Joe bloggs')
print('Names finally:', names)
print('last names in the list: %s' % names[-1])

#you can join lists using str.join() method

joined_names = '\n'.join(names)
print('\nList of names:')
print(joined_names)