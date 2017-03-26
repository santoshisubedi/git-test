#you can careate new lists by processing existing list.
words = ['This', 'Is', 'Just','A', 'Test']
capitalized_words = [x.capitalize() for x in words]

print('words:', words)
print('capitalized words:', capitalized_words)

#can use it for filtering the list items as well.
words = ['hello','world', 'Foo', 'bar', 'test', 'python', 'is','awesome']
short_words = [x for x in words if len(x) <=3]
other_words = [x for x in words if x not in short_words]
words_with_e = [x for x in words if x.count('e') >=1]
print('words:', words)
print('short words:', short_words)
print('other words:', other_words)
print('words with "e":', words_with_e)
