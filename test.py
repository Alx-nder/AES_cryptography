import aes

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
print(10<<2)
#rightshift 
print(10>>2)
