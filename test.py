import binascii
'''
#bitwise xor turns to binary first 
a = 12
b = 21
c = a ^ b
print(c)

# not operator
num=1
# num as a binary
# twos complement is 1's complement plus 1 
# NB CANNOT SUBTRACT A BINARY 
not_num=~num
# ~12 in binary is -13(int)
print(not_num)


# bitwise and
x=10
y=8
print(x&y)

#bitwise or  
print(x|y)

#bit wise leftshift binary number then add trailing zeros
print(10<<4)
#rightshift 
print(10>>2)

#turns a hex(base 16) to a int
print(int("a1",16))

#returns a hex denoted by the leading 0x
print(hex(161))

# Binary to Text
binary_data = b'I am text.'
text = binary_data.decode('utf-8')
print(text)

binary_data = bytes([65, 66, 67])  # ASCII values for A, B, C
text = binary_data.decode('utf-8')
print(text)

# Starting with a hex string you can unhexlify it to bytes
deadbeef = binascii.unhexlify('DEADBEEF')
print(deadbeef)

# Given raw bytes, get an ASCII string representing the hex values
hex_data = binascii.hexlify(b'\x00\xff')  # Two bytes values 0 and 255

# The resulting value will be an ASCII string but it will be a bytes type
# It may be necessary to decode it to a regular string
text_string = hex_data.decode('utf-8')  # Result is string "00ff"
print(text_string)


a_byte = b'\xff'  # 255
i = ord(a_byte)   # Get the integer value of the byte

bin = "{0:b}".format(i) # binary: 11111111
hex = "{0:x}".format(i) # hexadecimal: ff
oct = "{0:o}".format(i) # octal: 377

print(bin)
print(hex)
print(oct)

plaintext=b"sixteen char txt"
print(chr(plaintext[0]))      #use chr() to get the unicode of the byte-int
    
'''
def multiply_by_2(v):
    # leftshift adds a zero at end
    s = v << 1
    # this is to say s = s & 1111 1111 done to set particular bits to zero
    s &= 0xff
    # 128 is 2**7 or 8 bits 1000 0000

    # 101
    # 0000 1010
    # 1111 1111
    # 0000 1010 
 

    # 0000 0101
    # 1000 0000
    # 0000 0000

    # 0000 1010 
    # 0001 1011
    # 0001 1010

    if (v & 128) != 0:
        s = s ^ 0x1b
    return s
def rotate_row_left(row, n=1):
    return row[n:] + row[:n]

print(0x1b^0x11b)
# 0000 0001 1011
# 0001 0001 1011
# 0001 0000 0000