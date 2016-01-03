import wiringpi2 as wiringpi
import time
import schedule
import datetime
import sys

# String argument overwrite the time
WAKEUP_TIME_STR = sys.argv[1]
WAKEUP_TIME_STR_SPLIT = WAKEUP_TIME_STR.split(":",2)
WAKEUP_TIME_STR_HOUR = int(WAKEUP_TIME_STR_SPLIT[0])
WAKEUP_TIME_STR_MINUTE = int(WAKEUP_TIME_STR_SPLIT[1])

WAKEUP_TIME_DT = datetime.datetime(100,1,1,WAKEUP_TIME_STR_HOUR,WAKEUP_TIME_STR_MINUTE,00)
SUNRISE_START_DT = WAKEUP_TIME_DT - datetime.timedelta(0,20*60) # days, seconds, then other fields.
WAKEUP_TIME_DT = WAKEUP_TIME_DT.time() 
SUNRISE_START_DT = SUNRISE_START_DT.time()

print WAKEUP_TIME_DT
print SUNRISE_START_DT

# GENERATE TIME STR FROM BTIME
SUNRISE_START_STR = ""
if (SUNRISE_START_DT.hour<2):
	SUNRISE_START_STR = "0";
SUNRISE_START_STR = SUNRISE_START_STR + str(SUNRISE_START_DT.hour)

SUNRISE_START_STR = SUNRISE_START_STR + ":";

if (SUNRISE_START_DT.minute<2):
        SUNRISE_START_STR = "0";
SUNRISE_START_STR = SUNRISE_START_STR + str(SUNRISE_START_DT.minute)
print SUNRISE_START_STR

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
schedule.every().monday.at(SUNRISE_START_STR).do(RiseAndShine);
schedule.every().thuesday.at(SUNRISE_START_STR).do(RiseAndShine);
schedule.every().wednesday.at(SUNRISE_START_STR).do(RiseAndShine);
schedule.every().thursday.at(SUNRISE_START_STR).do(RiseAndShine);
schedule.every().friday.at(SUNRISE_START_STR).do(RiseAndShine);

			
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

	time.sleep(30)

