import calendar
import time
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :"
print(localtime)

cal = calendar.month(2018, 8)
print "Here is the calendar:"
print (cal)
