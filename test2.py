import RPi.GPIO as GPIO
import time

DEBUG = False

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

servo = GPIO.PWM(12, 500)

servo.start(0)

def backandforth():
    try:
        while True:
            if DEBUG:
                angle = int(input('set angle: '))
                servo.ChangeDutyCycle(angle)
            else:
                for dc in range(50,75,5):
                    servo.ChangeDutyCycle(dc)
                    print(dc)
                    time.sleep(2)
                for dc in range(75,50,-5):
                    servo.ChangeDutyCycle(dc)
                    time.sleep(2)
                    print(dc)
                    
    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()

backandforth()

