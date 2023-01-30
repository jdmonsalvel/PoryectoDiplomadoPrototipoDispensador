from machine import Pin
from time import sleep
import puerta 
import utime
import grameras as gramera
import servoSG90 as servo
import puerta
import wifi_connect as wifi
import dispensar 
from utime import sleep, sleep_ms

# digital input on pin 26
pir = Pin(5, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
servo.servoSG90(26, 75)
servo.servoSG90(25, 0)
servo.servoSG90(33, 0)
wifi.connect('Familia Arce_ETB', 'Alicia9314!')

def programar_dispensado(hora_inicio, hora_fin, num_ejecuciones):
    contador = 0
    intervalo = (hora_fin - hora_inicio) / num_ejecuciones
    while True:
        hora_actual = utime.localtime()[3]
        if hora_inicio <= hora_actual < hora_fin:
            if contador < num_ejecuciones:
                check_dispense()
                contador += 1
                utime.sleep(intervalo * 60 * 60)
            else:
                contador = 0
                utime.sleep(1*60*60)
        else:
            utime.sleep(1*60*60)

while True:
  pirVal = pir.value()
  if pirVal == 1:
      open_door()  
  if pirVal == 0 and doorStatus == "closed":
      print("Puerta Cerrada")
  else:
      close_door()
  sleep(1.0)


mensaje={"gramosConsumidos" : 5, "fecha": "28/01/2023", "hora":"07:00"}



firebase.setURL("https://prototipoproyecto-c2536-default-rtdb.firebaseio.com/")
firebase.put(datosDeConsumo/{}.format(str(valor)), mensaje, bg=0)
firebase.get()