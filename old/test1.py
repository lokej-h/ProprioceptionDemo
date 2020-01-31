import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

state = 'off'

def wait_for_button_up(pin):
    while GPIO.input(pin) == GPIO.HIGH:
            pass
    time.sleep(.2)

while True:
    if GPIO.input(10) == GPIO.HIGH and state == 'off':
        print("state on")
        state = 'on'
        wait_for_button_up(10)
        
    if GPIO.input(10) == GPIO.HIGH and state == 'on':
        print("state off")
        state = 'off'
        wait_for_button_up(10)
        
