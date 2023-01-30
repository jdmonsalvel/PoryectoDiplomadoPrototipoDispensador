import servoSG90 as servo
import grameras as gramera
from machine import Pin
from time import sleep
import ufirebase as firebase
import wifi_connect as wifi 

motor = servo.servo1 

global weight_on_open_plate, door_status
weight_on_open_plate = 0
contador = 0

        
def open_door():
    global weight_on_open_plate 
    weight_on_open_plate = gramera.peso(gramera.sensor1)
    print("puerta abierta")
    print("peso al abrir puerta: " + str(weight_on_open_plate))
    servo.SG90(motor, 0)
    sleep(10)


def close_door():
    global contador
    sleep(3)
    servo.SG90(motor, 75)
    weight_on_closed_plate = gramera.peso(gramera.sensor1)
    print("peso al cerrar puerta: " + str(weight_on_closed_plate))
    weight_difference = weight_on_open_plate - weight_on_closed_plate
    if weight_difference <= 0:
        print (weight_difference)
        print("no hay diferencia de peso")
    else:
        print("Diferencia de peso: " + str(weight_difference))
        fecha = wifi.FechaHora().fecha()
        hora = wifi.FechaHora().hora()
        message = {"gramosConsumidos" : weight_difference, "fecha": fecha, "hora": hora}
        contador = contador + 1
        firebase.put("datosDeConsumo/{}".format(str(contador)), message, bg=0)




