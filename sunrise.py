import wiringpi2 as wiringpi
import time
import schedule
import datetime
import sys

# String argument overwrite the time
SUNRISE_START_TIME = "05:45"
SUNRISE_START_TIME = sys.argv[1]
SST_SPLIT = SUNRISE_START_TIME.split(":",2)

a = datetime.datetime(100,1,1,int(SST_SPLIT[0]),int(SST_SPLIT[1]),59)
b = a - datetime.timedelta(0,20*60) # days, seconds, then other fields.

atime = a.time()
btime = b.time()

print atime
print btime

# GENERATE TIME STR FROM BTIME
SUNRISE_TIME = ""
if (btime.hour<2):
	SUNRISE_TIME = "0";
SUNRISE_TIME = SUNRISE_TIME + str(btime.hour)

SUNRISE_TIME = SUNRISE_TIME + ":";

if (btime.minute<2):
        SUNRISE_TIME = "0";
SUNRISE_TIME = SUNRISE_TIME + str(btime.minute)
print SUNRISE_TIME

# Constants
PWM_PIN = 18
LIGHT_INTENSITY = [1,1,1,2,2,3,3,5,6,7,8,9,10,12,14,16,18,20,25,30,35,40,50,60,70,80,100,120,140,160,200,250,300,450,625,850,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024,1024]

# Counter
global ii;
ii = 0;
global dawn;
dawn=False;

def RiseAndShine():
        global dawn;
        dawn=True;

# Init 
wiringpi.wiringPiSetupGpio()                    # set up GPIO numbering
wiringpi.pinMode(PWM_PIN, 2)
schedule.every().day.at(SUNRISE_TIME).do(RiseAndShine);
			
while True:
	schedule.run_pending()
	print ii 
	if (dawn and ii <=49):
		print ii
		ii = ii + 1;
		wiringpi.pwmWrite(PWM_PIN,LIGHT_INTENSITY[ii])
		print("Updated light intensity")
		timert = datetime.datetime.now()
		print timert.time()
	else: 	
		wiringpi.pwmWrite(PWM_PIN,0) 	
		dawn = False;
		print "I hope you have woken since i am out of here"		

	time.sleep(30)

