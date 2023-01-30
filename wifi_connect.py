import network
import time
import ntptime
from machine import RTC

def connect(ssid, key):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid, key)
        print('Connecting to: %s' % ssid)
        timeout = time.ticks_ms()
        while not wlan.isconnected():
            if (time.ticks_diff (time.ticks_ms(), timeout) > 10000):
                break
        if wlan.isconnected():
            print('Successful connection to: %s' % ssid)
            print('IP: %s\n' % wlan.ifconfig()[0])
        else:
            wlan.active(False)
            print('Failed to connect to: %s' % ssid)
    else:
        print('Connected\nIP: %s\n' % wlan.ifconfig()[0])
    ntptime.settime()
    (year, month, day, weekday, hour, minute, second, milisecond) = RTC().datetime() 
    RTC().init((year, month, day, weekday, hour-5, minute, second, milisecond))

class FechaHora:
    def fecha(self):
        return "{:02d}/{:02d}/{}".format(RTC().datetime()[2], RTC().datetime()[1], RTC().datetime()[0])

    def hora(self):
        return "{:02d}:{:02d}:{:02d}".format(RTC().datetime()[4], RTC().datetime()[5], RTC().datetime()[6])

