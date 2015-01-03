import sys
from datetime import date

yr = int(raw_input('Enter the year you were born:'))
mon = int(raw_input('Enter the month you were born:'))
dat = int(raw_input('Enter the date you were born:'))

birthday = date(yr,mon,dat)

now = date.today()
age = now - birthday

print "You are %d years old " %(age.days/365)
print "You've lived %d days" %(age.days)
