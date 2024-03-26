
v = 0.5

print(f'glifos v{v}')

from fuentes import CHARSET_SMALL as CHARSET
from utime import sleep_ms
from machine import SoftI2C, Pin

# Import the HT16K33 LED matrix module.
from hybotics_ht16k33 import matrix


# Create the I2C interface.
i2c = SoftI2C(sda=Pin(13), scl=Pin(14))

matrix = None

def init_matrix():
    global matrix
    
    if matrix == None:
        from hybotics_ht16k33 import matrix
        matrix = matrix.Matrix16x8(i2c,address=0x71)

def show_char(char,x=0,y=0,height=7,debug=False ):

    n_glifo = ord(char)-32
    if debug:
        print(char,n_glifo,end=' ')
    glifos = CHARSET[n_glifo]
    if debug:
        print(glifos,end=' ')
    for glifo in glifos:
        if debug:
            print(bin(glifo),end=' ')
        for i in range(8): 
            matrix[x,height-(y+i)] = glifo & 1
            glifo //= 2 # rotamos
        x += 1
    if debug:
        print()
    return x,y

def show_text(text,x=0,y=0,height=7,espacio=True, debug=False ):
    init_matrix()
    last_auto_write =  matrix.auto_write
    matrix.auto_write = False    
    matrix.fill(0)
    for char in text:
        x,y = show_char(char,x=x,y=y,height=height,debug=debug)
        if espacio:
            x+=1
    if last_auto_write == True:
        matrix.show()
    matrix.auto_write = last_auto_write
    
def show_charset(pausa = 500, height=7,debug=False):
    init_matrix()     
    for i in range(32,128):
        char = chr(i)
        print(char)
        show_char(char,height=height,debug=debug)
        sleep_ms(pausa)
        matrix.fill(0)

def show_number(numero,height=7):
    show_text(str(numero),height=height)

ojos_vacios =[  0b0011110000111100,
                0b0100001001000010,
                0b0100001001000010,
                0b0100001001000010,
                0b0100001001000010,
                0b0011110000111100]

ojos_abiertos =[0b0011110000111100,
                0b0100001001000010,
                0b0101101001011010,
                0b0101101001011010,
                0b0100001001000010,
                0b0011110000111100]

ojos_pequeños = [0b0011110000111100,
                 0b0100001001000010,
                 0b0100001001000010,
                 0b0011110000111100]

pupila = [0b11,0b11]


ojos_cerrados = [0,0,
                 0b0111111001111110,
                 0b0111111001111110,
                 0,0]

def show_bin_line(valor,x=0,y=0,width=16):
    for j in range(width):
        bit = valor & 1
        #print(x+j,y,bit)
        matrix[x+j,y] = bit
        valor //= 2

def show_image(image,x=0,y=0,width=16):
    init_matrix()
    last_auto_write =  matrix.auto_write
    matrix.auto_write = False
    #matrix.fill(0)
    image.reverse()
    for valor in image:
        #print(bin(valor))
        show_bin_line(valor,x=x,y=y,width=width)
        y += 1
    if last_auto_write ==True:
        matrix.show()
    matrix.auto_write = last_auto_write
    
def parpadeo(espera = 200):
    show_image(ojos_abiertos)
    sleep_ms(espera)
    show_image(ojos_cerrados)
    sleep_ms(espera)
    show_image(ojos_abiertos)
    sleep_ms(espera)

def show_ojos_pupila(x_base,y=3):
    last_auto_write =  matrix.auto_write
    matrix.auto_write = False
    matrix.fill(0)
    show_image(ojos_vacios)
    show_image(pupila, x=x_base, y=y, width=2)
    show_image(pupila, x=x_base+8, y=y, width=2)       
    matrix.show()
    matrix.auto_write =   last_auto_write      

def movimiento_bajo_pupila(espera = 300):
    show_image(ojos_vacios)
    for x_base in range(2,5):
        show_ojos_pupila(x_base)
        sleep_ms(espera)
        
def test_numbers():
    init_matrix()
    matrix.fill(1)
    sleep_ms(1000)
    show_text('0123',height=5)
    sleep_ms(1000)
    show_number(4567,height=5)
    sleep_ms(1000)
    show_text('8910',height=5)
    
def humm(espera = 300):
    show_image(ojos_vacios)
    sleep_ms(espera)
    matrix.shift_left()
    sleep_ms(espera)
    matrix.shift_right()
    show_image(ojos_cerrados)
    sleep_ms(espera)
    movimiento_bajo_pupila()
    sleep_ms(espera)
    matrix.fill(0)
    show_image(ojos_pequeños,x=1,y=1)
    sleep_ms(espera)
    show_ojos_pupila(4)    
    sleep_ms(espera)
    show_ojos_pupila(4,y=4)


def tests():
    #show_charset(pausa=300)  
    show_text('dadi',debug=True)
    sleep_ms(1000)
    test_numbers()
    # parpadeo()
    humm()
