from machine import Pin
from time import sleep
import servoSG90 as servo
import grameras as gramera

sensor1 = gramera.sensor1
sensor2 = gramera.sensor2

weightPlate = 35
weightproportion = 50
totalweight = weightPlate + weightproportion
def dispense():
    weightOnOpenPlate = gramera.peso(sensor1) - weightPlate
    weightToDespense = weightproportion - weightOnOpenPlate
    if weightOnOpenPlate <= weightproportion:
        print("cargo")
        servo.SG90(25,18)
        sleep(0.5)
        servo.SG90(25, 0)
        sleep(0.5)
        if gramera.peso(sensor2) >= weightToDespense:
            print("sirvio")
            sleep(1)
            servo.SG90(33, 80)
            sleep(1)
            servo.SG90(33, 0)
        else:
            print("Volvio a cargar y servir")
            servo.SG90(25, 0)
            sleep(1)
            servo.SG90(25,45)
            sleep(1)
            servo.SG90(25, 0)
            sleep(1)
            servo.SG90(33, 80)
            sleep(1)
            servo.SG90(33, 0)

def check_dispense():
    weightOnOpenPlate = gramera.peso(sensor1) - weightPlate
    if weightOnOpenPlate <= weightproportion:
        dispense()
    else:
        print("el plato tiene " + str(weightOnOpenPlate) + " gramos de comida")
        print("No se dispensa")
    
    
    
    
    
