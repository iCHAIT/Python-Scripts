import sys
from datetime import date

try:
    birthday = date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

    now = date.today()
    age = now - birthday

    print "You are %d years old " % (age.days / 365)
    print "You've lived %d days" % (age.days)

except ValueError, err:
    print 'ERROR:', err
