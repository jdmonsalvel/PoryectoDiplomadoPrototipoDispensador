
from machine import Pin, PWM
from utime import sleep, sleep_ms

servo1 = 26
servo2 = 25
servo3 = 33

def SG90(pin, angle):
    servo = PWM(Pin(pin), freq=50)
    if angle >=0 and angle<=360:
        angle = int((angle - 0) * (125- 25) / (180 - 0) + 25)
        servo.duty(angle)
    else:
        print("error, Angulo no contemplado, Digite entre 0 y 360")
    
