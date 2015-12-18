import wiringpi2 as wiringpi
import time
import schedule

# Init
PWM_PIN = 18
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PWM_PIN, 2)
wiringpi.pwmWrite(18, 0)    # duty cycle between 0 and 1024. 0 = off, 1024 = fully on
time.sleep(5)
wiringpi.pwmWrite(18, 10)
time.sleep(1)
wiringpi.pwmWrite(18, 20)
time.sleep(1)
wiringpi.pwmWrite(18, 40)
time.sleep(1)
wiringpi.pwmWrite(18, 60)
time.sleep(1)
wiringpi.pwmWrite(18, 100)
time.sleep(1)
wiringpi.pwmWrite(18, 200)
time.sleep(1)
wiringpi.pwmWrite(18, 300)
time.sleep(1)
wiringpi.pwmWrite(18, 10)
time.sleep(1)
wiringpi.pwmWrite(18, 500)
time.sleep(1)
wiringpi.pwmWrite(18, 750)
time.sleep(1)
wiringpi.pwmWrite(18, 1024)
time.sleep(1)
wiringpi.pwmWrite(18,0)
