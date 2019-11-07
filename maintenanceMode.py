# written by lokej-h
# last modified Thur Nov 7 2019

'''Supplies a maintenance mode for the servo'''

def menu():
    menu = '''
----------------------------------------------------------------|
|                   Welcome to Maintenance Mode                 |
|                                                               |
|   1: manual servo movement                                    |
|   2: retract fully                                            |
|   3: extend fully                                             |
|   4: move to midpoint                                         |
|   5: run continuous back and forth (Ctrl-C to return here)    |
|                                                               |
|   0: quit                                                     |
|                                                               |
|---------------------------------------------------------------|
'''
    while True:
        print(menu)
        selection = input("Selection: ")
        if selection in '012345':
            return selection
        print("input is not valid")


def manualMovement(pi, pin):
    try:
        while True:
            pwm = int(input("set pwm (1000-2000, or 0): "))
            pi.set_servo_pulse_width(pin, pwm)
    except KeyboardException:
        return

if __name__ == '__main__':
    selection = menu()
