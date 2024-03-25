# Frenove 4WD car con ESP32

![](./images/freenove_4WD.png)

## Pinout

![](./images/Pinout.jpeg)

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

PCF8574 (I2C)  0x20| GPIO
---|---
Track channel 1 |PO
Track channel 2 |P1
Track channel 3 |P2

PCA9685 (I2C)  | GPIO
---|---
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


ESP32 Camera| GPIO
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

Matrix VK16K33 0x70 ¿0x71?
-------------

Battery
-------
PIN_BATTERY 32      
LOW_VOLTAGE_VALUE  2100      //

## Python modules

### PWM driver - PCA9665
[PWM driver - PCA9665 - code](https://github.com/adafruit/micropython-adafruit-pca9685)

### LED matrix display 16 x 8 HT16K33

[Display - HT16K33 - code ](https://github.com/smittytone/HT16K33-Python)

[Documentación HT16K33](https://smittytone.net/docs/ht16k33.html)

### Cámara

[micropython camera firmware](https://github.com/lemariva/micropython-camera-driver/blob/master/README.md)