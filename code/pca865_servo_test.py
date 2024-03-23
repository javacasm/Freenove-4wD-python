# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

from time import sleep_ms
from machine import Pin, SoftI2C
from micropython_pca9685 import PCA9685, Servo

i2c = SoftI2C( sda=Pin(13), scl=Pin(14))  

print(i2c.scan())

pca = PCA9685(i2c,address = 0x5F)
servo8 = Servo(pca.channels[7])
servoh = Servo(pca.channels[0])
servov = Servo(pca.channels[1])

pca.frequency = 50
# We sleep in the loops to give the servo time to move into position.

for i in range(0,180):
    servo8.angle = i
    print(f'servoh {i}  ',end='\r')
    sleep_ms(30)
servo8.angle = 90    
'''
print() 
for i in range(30,150):
    servov.angle = i
    print(f'servov {i}  ',end='\r')    
    sleep_ms(30)

# You can also specify the movement fractionally.
fraction = 0.0
while fraction < 1.0:
    servo8.fraction = fraction
    fraction += 0.01
    sleep_ms(60)

pca.deinit()
'''
