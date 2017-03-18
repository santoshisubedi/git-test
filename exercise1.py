a = raw_input('enter the marks of C')
b = raw_input('enter the marks of IT')
c = raw_input('enter the marks of DAA')
d = raw_input('enter the marks of DL')
e = raw_input('enter the marks of SAD')

total = float(a) +float(b) + float(c) + float(d) + float(e)
print'total marks,total'
percentage =(total/5) * 100
print 'total = {}' .format(total)
print 'percentage = {:.2f} %'.format(percentage)