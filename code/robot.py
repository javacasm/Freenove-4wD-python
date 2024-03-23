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

PCA9685 I2C 0x5F
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

v = '0.7.5'

print(f'Robot v{v}')

PIN_BATTERY = 32
N_LEDS_RGB = 12
PIN_LEDS_RGB = 32
PIN_LDR = 33 # 2 LDRs ¿in a current divider?
PIN_SDA = 13
PIN_SCL = 14
PIN_TRIGGER = 12
PIN_ECHO = 15

# Salidas motores

M2_IN2 = 8
M2_IN1 = 9
M4_IN1 = 10
M4_IN2 = 11
M3_IN1 = 12
M3_IN2 = 13
M1_IN2 = 14
M1_IN1 = 15

motores = [[15,14],[9,8],[12,13],[10,11]]

from machine import Pin, SoftI2C, ADC, PWM
from neopixel import NeoPixel
from time import sleep_ms, time


MAX_COLOR = 50
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (MAX_COLOR,MAX_COLOR,MAX_COLOR)
COLOR_RED = (MAX_COLOR,0,0)
COLOR_GREEN = (0,MAX_COLOR,0)
COLOR_BLUE = (0,0,MAX_COLOR)

leds_RGB = NeoPixel(Pin(PIN_LEDS_RGB), N_LEDS_RGB)

i2c = SoftI2C(sda = Pin(PIN_SDA), scl = Pin(PIN_SCL))

LOW_VOLTAGE_BATTERY = 2100      #Set the minimum battery voltage

batteryCoefficient = 3.4   # Set the proportional coefficient

battery_ADC = ADC(Pin(PIN_BATTERY))

def get_battery_value(N_samples = 10):
    batteryADC_value = 0
    for i in range(N_samples):
        batteryADC_value += battery_ADC.read()
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
        sleep_ms(pause)

def run_color(colorLED = COLOR_BLUE, colorBack = COLOR_BLACK,
                   first_LED = 0, last_LED = N_LEDS_RGB,
                   step_LEDS = 1, pause = 50):
    for i in range(first_LED, last_LED, step_LEDS):
            set_leds_RGB_color(colorBack, False)
            leds_RGB[i] = colorLED
            leds_RGB.write()
            sleep_ms(pause)
            
def test_run_color(n_veces = 1, pause = 50):
    print('test led run')
    for j in range(n_veces):
        run_color(pause = pause)
        sleep_ms(300-50*j)
    for j in range(n_veces):
        run_color(pause = pause,colorLED = COLOR_RED,first_LED=N_LEDS_RGB-1,last_LED=-1,step_LEDS=-1)
        sleep_ms(300-50*j)
        

servos = None

def init_servos_old():
    from servo_pca9685 import Servos
    global servos
    servos = Servos(i2c, address=0x5F)
    
def test_servo_old():
    if servos == None:
        init_servos_old()
    for j in range(2):
        print(f'test servo {j}')
        for i in range(20,180):
            servos.position(j,degrees=i)
            print(j,i,end='\r')
            sleep_ms(100)

servoH = None
servoV = None

MIN_SERVO_H = 50
MAX_SERVO_H = 180
MIN_SERVO_V = 0
MAX_SERVO_V = 180

def init_servos_new():
    global servoH, servoV
    if servoV == None or servoV == None:
        from micropython_pca9685 import PCA9685, Servo    
        pca = PCA9685(i2c, address = 0x5F)
        pca.frequency = 50
        servoH = Servo(pca.channels[0])
        servoV = Servo(pca.channels[1])

def test_servo_new():
    init_servos_new()
    for i in range(MIN_SERVO_V, MAX_SERVO_V):
        servoV.angle = i
        print(f'servoV {i}  ',end='\r')
        sleep_ms(30)        
    for i in range(MIN_SERVO_H, MAX_SERVO_H):
        servoH.angle = i
        print(f'servoH {i}  ',end='\r')
        sleep_ms(30)
    set_servos()

def set_servos(posH = (MIN_SERVO_V + MAX_SERVO_V)//2, posV = (MIN_SERVO_V + MAX_SERVO_V)//2):
    init_servos_new()
    servoV.angle = posV
    servoH.angle = posH
        
pca9685 = None

def init_pca9685():
    global pca9685
    from pca9685 import PCA9685 
    pca9685 = PCA9685(i2c, address=0x5F)
    pca9685.freq(1500)


def set_speed_motor(i,speed):
    if pca9685 == None:
        init_pca9685()
        
    if speed < 0:
        pca9685.duty(motores[i][0],0)
        pca9685.duty(motores[i][1],abs(speed))
    else:
        pca9685.duty(motores[i][0],speed)
        pca9685.duty(motores[i][1],0)


def set_robot_turn(speed):
    set_speed_motor(0,speed)
    set_speed_motor(1,speed)
    set_speed_motor(2, -speed)
    set_speed_motor(3, -speed)
    
def set_robot_moves(speed):
    for i in range(4):
        set_speed_motor(i,speed)    

def test_motores():
    for i in range(4):
        for speed in range(-4000,4000,100):
            set_speed_motor(i,speed)
            sleep_ms(30)
            print(f'motor[{i}] - {speed}   ',end='\r')
        set_speed_motor(i,0)
        print(f'motor[{i}] STOP   ')
    

def test_robot_moves(duracion = 2000):
    # forward
    print('forward')
    set_robot_moves(4000)
    sleep_ms(duracion)
    print('backward')
    set_robot_moves(-4000)
    sleep_ms(duracion)
    print('Turn')
    set_robot_turn(3000)
    sleep_ms(duracion)
    print('Stop')
    set_robot_moves(0)
    
ldr = ADC(Pin(PIN_LDR), atten=ADC.ATTN_11DB)
MAX_LDR = 4000

def test_LDR(duracion = 10):
    global MAX_LDR
    print('Testing LDR')
    init_time = time()
    while time()-init_time < duracion:
        value_LDR = ldr.read()
        print(f'{value_LDR}   {duracion - int(time()-init_time)}s   ',end='\r')
        if MAX_LDR < value_LDR:
            MAX_LDR = value_LDR
            print(f'MAX_LDR {MAX_LDR}')
        sleep_ms(50)        

def move_servoH_by_LDR(duracion = 10, N = 40):
    print('Move servoH by LDR value')
    init_servos_new()
    init_time = time()

    while time()-init_time < duracion:
        
        media = 0
        for i in range(N):
            value_LDR = ldr.read()
            media += value_LDR
            print(f'{value_LDR}   {duracion - int(time()-init_time)}s   ',end='\r')
        media /= N 
        servoH.angle = 180 - (MAX_LDR - media)*(MAX_SERVO_H - MIN_SERVO_H)/MAX_LDR
        sleep_ms(10)
        
    set_servos()

pcf = None

def init_pcf8574():
    global pcf
    if pcf == None:
        from pcf8574 import PCF8574
        pcf = PCF8574(i2c, 0x20)
        
def test_pcf(duracion = 10):
    print('Testing PCF8574 (line tracking)')
    init_pcf8574()
    init_time = time()

    while time()-init_time < duracion:
        print(f'{pcf.pin(0)} {pcf.pin(1)} {pcf.pin(2)}',end = '\r')
        sleep_ms(50)
        
matrix = None

def init_matrix():
    global matrix
    
    if matrix == None:
        from hybotics_ht16k33 import matrix
        matrix = matrix.Matrix16x8(i2c,address=0x71)
        
def test_matrix(duracion = 10):
    print('testing led matrix')
    init_matrix()
    matrix.fill(0)

    # Set a pixel in the origin 0, 0 position.
    matrix[0, 0] = 1
    # Set a pixel in the middle 8, 4 position.
    matrix[8, 4] = 1
    # Set a pixel in the opposite 15, 7 position.
    matrix[15, 7] = 1

    sleep_ms(200)

    # Draw a Smiley Face
    matrix.fill(0)

    for row in range(2, 6):
        matrix[row, 0] = 1
        matrix[row, 7] = 1

    for column in range(2, 6):
        matrix[0, column] = 1
        matrix[7, column] = 1

    matrix[1, 1] = 1
    matrix[1, 6] = 1
    matrix[6, 1] = 1
    matrix[6, 6] = 1
    matrix[2, 5] = 1
    matrix[5, 5] = 1
    matrix[2, 3] = 1
    matrix[5, 3] = 1
    matrix[3, 2] = 1
    matrix[4, 2] = 1

    # Move the Smiley Face Around
    init_time = time()

    while time()-init_time < duracion:
        for frame in range(0, 8):
            matrix.shift_right(True)
            sleep_ms(50)
        for frame in range(0, 8):
            matrix.shift_down(True)
            sleep_ms(50)
        for frame in range(0, 8):
            matrix.shift_left(True)
            sleep_ms(50)
        for frame in range(0, 8):
            matrix.shift_up(True)
            sleep_ms(50)
    
def tests():
    test_fade_color(0,MAX_COLOR,1,5)
    test_fade_color(MAX_COLOR,-1,-1,5)
    test_run_color()
    set_leds_RGB_color(COLOR_BLACK)
    test_LDR()
    test_i2c()
    print(f'Battery: {get_battery_value()}')
    test_pcf()
    test_matrix()
    test_servo_new()
    move_servoH_by_LDR()
    test_motores()
    test_robot_moves()
    set_servos()
    
if __name__ == '__main__':
#    tests()
    test_matrix()
