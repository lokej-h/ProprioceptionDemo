import threading
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

state = 'off'

DEBUG = True

GPIO.setup(12, GPIO.OUT)

def backandforth():
    print("out")
    servo.ChangeDutyCycle(82)
    time.sleep(7)
    if state == 'off':
        return
    print("in")
    servo.ChangeDutyCycle(47)
    time.sleep(7)

def thread():
    t = threading.currentThread()
    while getattr(t, "do_run", True):        
        if DEBUG:
                angle = int(input('set angle: '))
                servo.ChangeDutyCycle(angle)
        else:
            while getattr(t, "do_run", True):
                backandforth()

            '''
            dc = 50
            while getattr(t, "do_run", True):
                servo.ChangeDutyCycle(dc)
                print(dc)
                time.sleep(1)
                if dc == 75:
                    count = 'down'
                if dc == 50:
                    count = 'up'
                if count == 'up':
                    dc += 5
                else:
                    dc -= 5
            '''




servo = GPIO.PWM(12, 500)
t = threading.Thread(target=thread)
t.do_run = False
t.start()
servo.start(0)
servo.ChangeDutyCycle(47)
time.sleep(3)
servo.ChangeDutyCycle(0)
print("ready")




def wait_for_button_up(pin):
    while GPIO.input(pin) == GPIO.HIGH:
            pass
    time.sleep(.2)

try:
    while True:
        if GPIO.input(10) == GPIO.HIGH and state == 'off':
            print("state on")
            state = 'on'
            t.do_run = True
            servo.start(0)
            wait_for_button_up(10)
            
        if GPIO.input(10) == GPIO.HIGH and state == 'on':
            print("state off")
            state = 'off'
            t.do_run = False
            servo.stop()
            wait_for_button_up(10)
            
            
except KeyboardInterrupt:
    print("stopping")
    t.do_run = False
    if t.is_alive():
        t.join()
    servo.stop()
    servo.start(0)
    servo.ChangeDutyCycle(47)
    time.sleep(7)


GPIO.cleanup()
servo.stop()

print("cleaned up")
