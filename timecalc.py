import datetime
import sys
print(sys.argv[1])
a = datetime.datetime(100,1,1,11,34,59)
b = a + datetime.timedelta(0,3) # days, seconds, then other fields.
print a.time()
print b.time()
