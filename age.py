dob = raw_input('enter your date of birth in YYYY-MM-DD format.')
dob = dob.split('-')
#calculate the date timestamp in years
dob_timestamp = float(dob[0]) + float(dob[1])/12 + float(dob[2])/365

#calculate the today's timestamp in years
today = ['2017', '03', '17']
today_timestamp = float(today[0]) + float(today[1])/12 + float(today[2])/365

#compute the differences
years = today_timestamp - dob_timestamp
months = (years - int(years)) *12
print 'your age is %d years %d months' % (years, months)