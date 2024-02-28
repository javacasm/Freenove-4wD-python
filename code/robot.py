'''
www.freenove.com


Freenove 4WD Car Board for ESP32
ESP32  | port
---|---
SDA | 13
SCL | 14
TRIG | 12
ECHO | 15
WS2812 | 32
Light ADC |  33
IR Receiver | 0
Buzzer | 2

PCF8574 (I2C)  0x20| port
---|---
Track channel 1 |PO
Track channel 2 |P1
Track channel 3 |P2

PCA9685 (I2C)  | port
Servo1 | LED0
Servo2 | LED1
Servo3 | LED2
Servo4 | LED3
Servo5 | LED4
Servo6 | LED5
Servo7 | LED6
Servo8 | LED7
M2_IN2 | LED8
M2_IN1 | LED9
M4_IN1 | LED10
M4_IN2 | LED11
M3_IN1 | LED12
M3_IN2 | LED13
M1_IN2 | LED14
M1_IN1 | LED15

PCA9685 I2C ¿0x5F?
-------
FREQUENCY          1000      //Define the operating frequency of servo
SERVO_0  0         //Define PCA9685 channel to control servo 1
SERVO_1  1         //Define the PCA9685 channel to control servo 2
SERVO_MIDDLE_POINT 1500      //Define the middle position of the servo   
MOTOR_SPEED_MIN   -4095      //Define a minimum speed limit for wheels
MOTOR_SPEED_MAX   4095


ESP32 Camera port
---|---
CSI_Y6 | 36
CSI Y7 | 39
CSI Y8 | 34
CSI Y9 | 35
CSI VYSNC | 25
SIOD | 26
SIOC | 27
CSI Y2 | 4
CSI Y3 | 5
CSI Y4 | 18
CSI Y5 | 19
XCLK | 21
PCLK | 22
HREF | 23

Matrix VK16K33 0x70
-------------

Battery
-------
PIN_BATTERY 32        //Set the battery detection voltage pin
LOW_VOLTAGE_VALUE  2100      //Set the minimum battery voltage

batteryCoefficient = 3.4   //Set the proportional coefficient

batteryADC = Get_Battery_Voltage_ADC();
  if (batteryADC <= LOW_VOLTAGE_VALUE):
    return 0

  batteryVoltage = (batteryADC / 4096.0  * 3.3 ) * batteryCoefficient

'''

v = 0.5

print(f'Robot v{v}')

PIN_BATTERY = 32
N_LEDS_RGB = 12
PIN_LEDS_RGB = 32
PIN_LDR = 33
PIN_SDA = 13
PIN_SCL = 14
PIN_TRIGGER = 12
PIN_ECHO = 15

import machine
import neopixel
import time


MAX_COLOR = 50
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (MAX_COLOR,MAX_COLOR,MAX_COLOR)
COLOR_RED = (MAX_COLOR,0,0)
COLOR_GREEN = (0,MAX_COLOR,0)
COLOR_BLUE = (0,0,MAX_COLOR)

leds_RGB = neopixel.NeoPixel(machine.Pin(PIN_LEDS_RGB), N_LEDS_RGB)

i2c = machine.SoftI2C(sda = machine.Pin(PIN_SDA), scl = machine.Pin(PIN_SCL))

LOW_VOLTAGE_BATTERY = 2100      #Set the minimum battery voltage

batteryCoefficient = 3.4   # Set the proportional coefficient

battery_ADC = machine.ADC(machine.Pin(PIN_BATTERY))

def get_battery_value(N_samples = 10):
    batteryADC_value = 0
    for i in range(N_samples):
        batteryADC_value += battery_ADC.read_u16()
    batteryADC_value /= N_samples
    
    if (batteryADC_value <= LOW_VOLTAGE_BATTERY):
        return 0

    batteryVoltage = (batteryADC_value / 4096.0  * 3.3 ) * batteryCoefficient
    return batteryVoltage

bDebug = False

def debug(string):
    if bDebug:
        print(string)

def set_leds_RGB_color(color, bWrite = True):
    debug(f'set_leds_RGB_color {color} , {bWrite}')
    for i in range(N_LEDS_RGB):
        leds_RGB[i] = color
    if bWrite:    
        leds_RGB.write()

def test_i2c():
    print('test i2c')
    for add in i2c.scan():
        dev_name = ''
        if add == 0x5F:
            dev_name = 'PCA9685'
        elif add == 0x20:
            dev_name = 'PCF8574'
        elif add == 0x70:
            dev_name = 'VK16K33'
        else:
            dev_name ='unkown'
        print(f' {add} - {hex(add)} - {dev_name} ') 
    
def test_fade_color(first_color = 0, max_color = MAX_COLOR, step_color=1, pause=50):
    print('test fade color')
    for i in range(first_color,max_color,step_color):
        set_leds_RGB_color((i,i,i))
        time.sleep_ms(pause)

def run_color(colorLED = COLOR_BLUE, colorBack = COLOR_BLACK,
                   first_LED = 0, last_LED = N_LEDS_RGB,
                   step_LEDS = 1, pause = 50):
    for i in range(first_LED, last_LED, step_LEDS):
            set_leds_RGB_color(colorBack, False)
            leds_RGB[i] = colorLED
            leds_RGB.write()
            time.sleep_ms(pause)
            
def test_run_color(n_veces = 1, pause = 50):
    print('test led run')
    for j in range(n_veces):
        run_color(pause = pause)
        time.sleep_ms(300-50*j)
    for j in range(n_veces):
        run_color(pause = pause,colorLED = COLOR_RED,first_LED=N_LEDS_RGB-1,last_LED=-1,step_LEDS=-1)
        time.sleep_ms(300-50*j)        
        
def tests():
    test_fade_color(0,MAX_COLOR,1,5)
    test_fade_color(MAX_COLOR,-1,-1,5)
    test_run_color()
    set_leds_RGB_color(COLOR_BLACK)
    test_i2c()
    print(f'Battery: {get_battery_value()}')

if __name__ == '__main__':
    tests()