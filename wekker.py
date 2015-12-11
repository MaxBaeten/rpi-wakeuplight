import schedule
import time

# Constants
global StateA;
global StateB;
global StateC1;
global StateC2;
global wakeup_time_start;
global wakeup_time_alarm;
StateA = True;
StateB = False;
StateC1 = False;
StateC2 = False;
wakeup_time_start = "5.10"
wakeup_time_alarm = "5.40"

# Functions
def alarm_on():
    print("BEEP BEEP BEEP WAKEUP!")

#def set_light_intensity(int intensity):
#    print("Setting the light intensity to:!"+intensity)

def wakeup():
	schedule.every().day.at(wakeup_time_start).do(job)

def BUTTON_IN_ACTIVATE_ALARM():
	global StateB;
	global StateA;
	
	StateA = not StateA;
	StateB = not StateB;
	
	if StateB:
		print("Activated Alarm")


def job():
    print("I'm working...")

# State machine
while True:
	
	#	State A: Inactive 
	if StateA:
		print("I'm in state A. Alarm is inactive")
	
	#	B: Active Alarm: Waiting for Sunrise
	if StateB:
		print("I'm in state B. Alarm is active yet the sun is not yet up")
	
	#	C1: Active Alarm: Sunrise
	if StateC1:
		print("I'm in state C1. The sun is rising")
	
	#	C2: Alarm: Wakeup    
	if StateC2:
		print("I'm in state C2. Alarm is going off")

	schedule.run_pending()
	time.sleep(2)
	
	
	BUTTON_IN_ACTIVATE_ALARM()

#	State machine
#
#	State A: Inactive 
#
#	State B: Active
#
#	State C: Active
#		C1: Sunrise
#		C2: Wakeup

#	State transitions:
#
# 	Activate alarm: (A->B)
#		Triggered by a button
#		Display 'On' on display	
#	Unactivate alarm: (B->A)
#		Triggered by a button
#		Display 'Off' on display
#
#	StartSunrise: (B1->B2)
#		Start by timer
#		
#	StartAlarm: (B2->B3)
#		Triggered by timer
#
#
#
#
#
# 	To do: 
# - Reinstall rpi and make sure enough space is there for the root file system and that the home folder is put on usb disk
# - Checkout repo on rpi
# - Read a button from gpio and print string
# - Read a button from gpio and execute function (Make sure to limit that execution to once every seond) 
# - Control a led with a transistor
# - Hook up a led to a button
# - Publish time om 4 digit display
# - Start on state machine
# - 
#
