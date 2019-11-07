import threading
import pigpio
import time
import os

def inits():
    '''initializes our gpio'''
    print("turning on GPIO deamon")
    os.system('sudo pigpiod')
    time.sleep(3)
    print("setting up GPIO")
    global pi
    pi = pigpio.pi()
    print("setting up button")
    pi.set_pull_up_down(15, pigpio.PUD_DOWN)
    pi.set_mode(15, pigpio.INPUT)
    print("setting up servo")
    pi.set_mode(18, pigpio.OUTPUT)
    print("\tmoving servo to a neutral postion, please wait")
    pi.set_servo_pulsewidth(18, 1010)
    time.sleep(3)
    print("\tassumed servo in position, PWM off")
    pi.set_servo_pulsewidth(18, 0)
    print("ready")
    
def cleanup():
    print("\n\ncleaning up")
    print("moving servo to home")
    pi.set_servo_pulsewidth(18, 1000)
    time.sleep(5)
    print("\tdone")
    print("turning off PWM")
    pi.set_servo_pulsewidth(18, 0)
    print("\tdone")
    print("cleanup complete")
    
def toggle_state():
    '''changes our "global" state'''
    global state
    state = not state

def backandforth():
    '''a simple function to move the servo back and forth'''
    print("extending servo")
    pi.set_servo_pulsewidth(18, 2000)
    time.sleep(2.5)
    print("retracting servo")
    pi.set_servo_pulsewidth(18, 1010)
    time.sleep(2.5)

def wait_for_button_up(pin):
    '''stalls the program until button up, will be replaced'''
    while GPIO.input(pin) == GPIO.HIGH:
            pass
    time.sleep(.2)

if __name__ == '__main__':
    try:
        inits()
        input("press Enter to start and Ctrl+C to quit")
        print("\n\tPress the button to extend and retract the servo")
        while True:
            #we wait for a button push, the ludicrous number is so that
            #it doesn't move every 60 sec
            pi.wait_for_edge(15, pigpio.RISING_EDGE, 99999999)
            backandforth()
    except KeyboardInterrupt:
        cleanup()
    input("Press Enter to close this window")
