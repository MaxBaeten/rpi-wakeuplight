import RPi.GPIO as GPIO
import time

GPIOPIN = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIOPIN, GPIO.OUT)
GPIO.output(GPIOPIN, False)

t=0;
while t<(1000.0):
	GPIO.output(GPIOPIN,True)
	time.sleep(0.01)
	GPIO.output(GPIOPIN,False)
	time.sleep(0.01)
	t=t+1;

print('Yeaaaaaaaaah')
while False:
        GPIO.output(GPIOPIN,True)
        time.sleep(0.01)
        GPIO.output(GPIOPIN,False)
        time.sleep(0.01)


p = GPIO.PWM(GPIOPIN,10000)

p.start(0)
print('Ready')

DC = 1;
while DC <= 100.0:
	p.ChangeDutyCycle(DC);
        time.sleep(2.5);
	DC = DC * 1.1;
        print('DutyCycle = ',DC)

print('Done')

p.stop()
GPIO.cleanup()
