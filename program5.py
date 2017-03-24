x = int(input("enter value of x"))
y= int(input("enter the value of y"))
if (x > 0) and (y > 0):
	print('it lies in the first quardant')
elif (x < 0) and (y > 0):
	print('it lies in the second quardent')
elif (x<0) and (y < 0):
	print ('it lies in the third quardent')
elif (x > 0) and (y < 0):
	print('it lies in the fourth quardent')
elif(x == 0) and (y == 0):
	print('it lies in origin')
elif(x == 0 and y>0):
	print('it lies in x-axis')
elif(x > 0 and y == 0) :
	print('it lies in y-axis')


