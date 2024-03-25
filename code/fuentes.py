v = 0.5

print(f'fuentes v{v}')
# from HT16K33-Python
CHARSET_BIG = [
        b"\x00\x00",              # space - Ascii 32
        b"\xfa",                  # !
        b"\xc0\x00\xc0",          # "
        b"\x24\x7e\x24\x7e\x24",  # #
        b"\x24\xd4\x56\x48",      # $
        b"\xc6\xc8\x10\x26\xc6",  # %
        b"\x6c\x92\x6a\x04\x0a",  # &
        b"\xc0",                  # '
        b"\x7c\x82",              # (
        b"\x82\x7c",              # )
        b"\x10\x7c\x38\x7c\x10",  # *
        b"\x10\x10\x7c\x10\x10",  # +
        b"\x06\x07",              # ,
        b"\x10\x10\x10\x10",      # -
        b"\x06\x06",              # .
        b"\x04\x08\x10\x20\x40",  # /
        b"\x7c\x8a\x92\xa2\x7c",  # 0 - Ascii 48
        b"\x42\xfe\x02",          # 1
        b"\x46\x8a\x92\x92\x62",  # 2
        b"\x44\x92\x92\x92\x6c",  # 3
        b"\x18\x28\x48\xfe\x08",  # 4
        b"\xf4\x92\x92\x92\x8c",  # 5
        b"\x3c\x52\x92\x92\x8c",  # 6
        b"\x80\x8e\x90\xa0\xc0",  # 7
        b"\x6c\x92\x92\x92\x6c",  # 8
        b"\x60\x92\x92\x94\x78",  # 9
        b"\x36\x36",              # : - Ascii 58
        b"\x36\x37",              #
        b"\x10\x28\x44\x82",      # <
        b"\x24\x24\x24\x24\x24",  # =
        b"\x82\x44\x28\x10",      # >
        b"\x60\x80\x9a\x90\x60",  # ?
        b"\x7c\x82\xba\xaa\x78",  # @
        b"\x7e\x90\x90\x90\x7e",  # A - Ascii 65
        b"\xfe\x92\x92\x92\x6c",  # B
        b"\x7c\x82\x82\x82\x44",  # C
        b"\xfe\x82\x82\x82\x7c",  # D
        b"\xfe\x92\x92\x92\x82",  # E
        b"\xfe\x90\x90\x90\x80",  # F
        b"\x7c\x82\x92\x92\x5c",  # G
        b"\xfe\x10\x10\x10\xfe",  # H
        b"\x82\xfe\x82",          # I
        b"\x0c\x02\x02\x02\xfc",  # J
        b"\xfe\x10\x28\x44\x82",  # K
        b"\xfe\x02\x02\x02",      # L
        b"\xfe\x40\x20\x40\xfe",  # M
        b"\xfe\x40\x20\x10\xfe",  # N
        b"\x7c\x82\x82\x82\x7c",  # O
        b"\xfe\x90\x90\x90\x60",  # P
        b"\x7c\x82\x92\x8c\x7a",  # Q
        b"\xfe\x90\x90\x98\x66",  # R
        b"\x64\x92\x92\x92\x4c",  # S
        b"\x80\x80\xfe\x80\x80",  # T
        b"\xfc\x02\x02\x02\xfc",  # U
        b"\xf8\x04\x02\x04\xf8",  # V
        b"\xfc\x02\x3c\x02\xfc",  # W
        b"\xc6\x28\x10\x28\xc6",  # X
        b"\xe0\x10\x0e\x10\xe0",  # Y
        b"\x86\x8a\x92\xa2\xc2",  # Z - Ascii 90
        b"\xfe\x82\x82",          # [
        b"\x40\x20\x10\x08\x04",  # \
        b"\x82\x82\xfe",          # ]
        b"\x20\x40\x80\x40\x20",  # ^
        b"\x02\x02\x02\x02\x02",  # _
        b"\xc0\xe0",              # '
        b"\x04\x2a\x2a\x1e",      # a - Ascii 97
        b"\xfe\x22\x22\x1c",      # b
        b"\x1c\x22\x22\x22",      # c
        b"\x1c\x22\x22\xfc",      # d
        b"\x1c\x2a\x2a\x10",      # e
        b"\x10\x7e\x90\x80",      # f
        b"\x18\x25\x25\x3e",      # g
        b"\xfe\x20\x20\x1e",      # h
        b"\xbc\x02",              # i
        b"\x02\x01\x21\xbe",      # j
        b"\xfe\x08\x14\x22",      # k
        b"\xfc\x02",              # l
        b"\x3e\x20\x18\x20\x1e",  # m
        b"\x3e\x20\x20 \x1e",     # n
        b"\x1c\x22\x22\x1c",      # o
        b"\x3f\x22\x22\x1c",      # p
        b"\x1c\x22\x22\x3f",      # q
        b"\x22\x1e\x20\x10",      # r
        b"\x12\x2a\x2a\x04",      # s
        b"\x20\x7c\x22\x04",      # t
        b"\x3c\x02\x02\x3e",      # u
        b"\x38\x04\x02\x04\x38",  # v
        b"\x3c\x06\x0c\x06\x3c",  # w
        b"\x22\x14\x08\x14\x22",  # x
        b"\x39\x05\x06\x3c",      # y
        b"\x26\x2a\x2a\x32",      # z - Ascii 122
        b"\x10\x7c\x82\x82",      #
        b"\xee",                  # |
        b"\x82\x82\x7c\x10",      #
        b"\x40\x80\x40\x80",      # ~
        b"\x60\x90\x90\x60"       # Degrees sign - Ascii 127
    ]
# la idea es hacer una fuente proporcional de 5 de alto
CHARSET_SMALL = [
        b"\x00\x00",              # space - Ascii 32
        b"\x7a",                  # !
        b"\xc0\x00\xc0",          # "
        b"\x24\x7e\x24\x7e\x24",  # #
        b"\x24\xd4\x56\x48",      # $
        b"\xc6\xc8\x10\x26\xc6",  # %
        b"\x6c\x92\x6a\x04\x0a",  # &
        b"\xc0",                  # '
        b"\x7c\x82",              # (
        b"\x82\x7c",              # )
        b"\x10\x7c\x38\x7c\x10",  # *
        b"\x10\x38\x10",  # +
        b"\x06\x07",              # ,
        b"\x10\x10\x10",      # -
        b"\x06\x06",              # .
        b"\x04\x08\x10\x20\x40",  # /
        b"\x1f\x11\x1f",  # 0 - Ascii 48
        b"\x1f",          # 1
        b"\x17\x15\x1d",  # 2
        b"\x15\x15\x1f",  # 3
        b"\x1c\x04\x0f",  # 4
        b"\x1d\x15\x17",  # 5
        b"\x1f\x15\x17",  # 6
        b"\x10\x13\x1c",  # 7
        b"\x1f\x15\x1f",  # 8
        b"\x1c\x14\x1f",  # 9
        b"\x36\x36",              # : - Ascii 58
        b"\x36\x37",              #
        b"\x10\x28\x44\x82",      # <
        b"\x24\x24\x24",  # =
        b"\x82\x44\x28\x10",      # >
        b"\x60\x80\x9a\x90\x60",  # ?
        b"\x7c\x82\xba\xaa\x78",  # @
        b"\x7e\x90\x7e",  # A - Ascii 65
        b"\xfe\x92\x6c",  # B
        b"\x7c\x82\x44",  # C
        b"\xfe\x82\x7c",  # D
        b"\xfe\x92\x82",  # E
        b"\xfe\x90\x80",  # F
        b"\x7c\x82\x92\x5c",  # G
        b"\xfe\x10\xfe",  # H
        b"\x82\xfe\x82",          # I
        b"\x0c\x02\xfc",  # J
        b"\xfe\x10\x28\x44\x82",  # K
        b"\xfe\x02",      # L
        b"\xfe\x40\x20\x40\xfe",  # M
        b"\xfe\x40\x20\x10\xfe",  # N
        b"\x7c\x82\x7c",  # O
        b"\xfe\x90\x60",  # P
        b"\x7c\x82\x92\x8c\x7a",  # Q
        b"\xfe\x90\x98\x66",  # R
        b"\x64\x92\x4c",  # S
        b"\x80\xfe\x80",  # T
        b"\xfc\x02\xfc",  # U
        b"\xf8\x04\x02\x04\xf8",  # V
        b"\xfc\x02\x3c\x02\xfc",  # W
        b"\xc6\x28\x10\x28\xc6",  # X
        b"\xe0\x10\x0e\x10\xe0",  # Y
        b"\x86\x8a\x92\xa2",  # Z - Ascii 90
        b"\xfe\x82",          # [
        b"\x40\x20\x10\x08\x04",  # \
        b"\x82\xfe",          # ]
        b"\x20\x40\x80\x40\x20",  # ^
        b"\x02\x02\x02",  # _
        b"\xc0\xe0",              # '
        b"\x08\x54\x3c",      # a - Ascii 97
        b"\xfe\x22\x1c",      # b
        b"\x1c\x22\x22",      # c
        b"\x1c\x14\xfc",      # d
        b"\x1c\x2a\x10",      # e
        b"\x10\x7e\x90",      # f
        b"\x18\x25\x3e",      # g
        b"\xfe\x20\x1e",      # h
        b"\x5c",              # i
        b"\x02\x01\x21\xbe",      # j
        b"\xfe\x08\x14\x22",      # k
        b"\xfc\x02",              # l
        b"\x3e\x20\x18\x20\x1e",  # m
        b"\x3e\x20 \x1e",     # n
        b"\x1c\x22\x1c",      # o
        b"\x3f\x22\x1c",      # p
        b"\x1c\x22\x3f",      # q
        b"\x22\x1e\x20\x10",      # r
        b"\x12\x2a\x04",      # s
        b"\x20\x7c\x22\x04",      # t
        b"\x3c\x02\x3e",      # u
        b"\x38\x04\x02\x04\x38",  # v
        b"\x3c\x06\x0c\x06\x3c",  # w
        b"\x22\x14\x08\x14\x22",  # x
        b"\x39\x05\x06\x3c",      # y
        b"\x26\x2a\x32",      # z - Ascii 122
        b"\x10\x7c\x82\x82",      #
        b"\xee",                  # |
        b"\x82\x82\x7c\x10",      #
        b"\x40\x80\x40\x80",      # ~
        b"\x60\x90\x90\x60"       # Degrees sign - Ascii 127
    ]
'''
img0 = ['111',
        '101',
        '101',
        '101',
        '111']
img1 = ['1',
        '1',
        '1',
        '1',
        '1']
img2 = ['111',
        '001',
        '111',
        '100',
        '111']
img3 = ['111',
        '001',
        '111',
        '001',
        '111']
img4 = ['100',
        '101',
        '111',
        '001',
        '001']
img5 = ['111',
        '100',
        '111',
        '001',
        '111']
img6 = ['111',
        '100',
        '111',
        '101',
        '111']
img7 = ['111',
        '001',
        '001',
        '010',
        '010']
img8 = ['111',
        '101',
        '111',
        '101',
        '111']
img9 = ['111',
        '101',
        '111',
        '001',
        '001']
numeros= [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]        
'''
def graf2glyfo(img,debug=False ):
    if debug:
        for i in img:
            print(i)
    alto = len(img)
    ancho = len(img[0])
    if debug:
        print(f'{alto}x{ancho}')
    glyfos = []
    for i in range(ancho):
        glyfo = 0
        peso = 2**(alto-1)
        for j in range(alto):
            if img[j][i]=='1':
                glyfo += peso
            peso//=2
        if debug:
            print(bin(glyfo))
        glyfos.append(glyfo)
    string='b"'
    for glyfo in glyfos:
        string_number= str(hex(glyfo))
        string += f'\\{string_number[1:]}'
    string+='"'
    if debug:
        print(string)
    return glyfos

if __name__ == '__main__':
    import text
'''    numeros= [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]
    for num in numeros:
        graf2glyfo(num,debug=True)
'''