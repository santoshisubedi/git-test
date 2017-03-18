equation = raw_input('equqtion: ')
#'y','mx+c'
rhs = equation.split('=')[1]

#'mx','c'
parts = rhs.split('+')
#parse out the values of m&c 
m = parts[0].replace('x', '').strip()
c = parts[1].strip()

#print them out
print 'slope of line :{}'.format(m)
print 'y-intercept :{}'.format(c)