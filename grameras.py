from machine import freq
from hx711 import HX711
from utime import sleep, sleep_ms
 
#sensor1, plato de comida
#sensor2, regulador de peso de dispensador 

sensor1 = HX711(d_out=19, pd_sck=18)
sensor2 = HX711(d_out=12, pd_sck=27)

def calcular_offset(sensor):
    sensor = sensor
    muestras = []
    for i in range(25):
        muestras.append(sensor.read())
    offset = sum(muestras) / len(muestras)
    sensor.offset = offset
    #print(offset)
    return offset

offset_sensor1 = calcular_offset(sensor1)
offset_sensor2 = calcular_offset(sensor2)

def peso(sensor):
    if sensor == sensor1:
        peso = int((sensor1.read()) /1000 - 404)
    if sensor == sensor2:
        peso = int((sensor2.read()) /1000 - 421)
    return peso
