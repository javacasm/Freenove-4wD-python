# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

v = 0.1

print(f'Boot v{v}')

import time
import config

import network

w = network.WLAN(network.STA_IF)
w.active(True)

if w.active() == False:
    w.active(True)

if w.isconnected() == False:
    w.connect(config.Wifi_SSID,config.Wifi_passwd)

while w.isconnected() == False:
    print('.')
    time.sleep_ms(500)
else:
    print(f'Conectado a {config.Wifi_SSID} IP:{w.ifconfig()[0]}')


import webrepl
webrepl.start()
