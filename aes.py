#https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf





"""Transformation in the Cipher and Inverse Cipher in which a Round 
Key is added to the State using an XOR operation. The length of a 
Round Key equals the size of the State (i.e., for Nb = 4, the Round 
Key length equals 128 bits/16 bytes)."""
def Add_RoundKey():
    return

"""Transformation in the Cipher that takes all of the columns of the 
State and mixes their data (independently of one another) to 
produce new columns."""
def Mix_Columns():
    return

"""Transformation in the Inverse Cipher that is the inverse of 
MixColumns()."""
def InvMixColumns():
    return

"""Transformation in the Cipher that processes the State by cyclically 
shifting the last three rows of the State by different offsets. """
def ShiftRows():
    return

"""Transformation in the Inverse Cipher that is the inverse of 
ShiftRows()."""
def InvShiftRows():
    return


"""Transformation in the Cipher that processes the State using a non-linear byte substitution table (S-box) that operates on each of the 
State bytes independently. """
def SubBytes():
    return
    
"""Transformation in the Inverse Cipher that is the inverse of 
SubBytes()."""
def InvSubBytes():
    return

"""Function used in the Key Expansion routine that takes a four-byte 
input word and applies an S-box to each of the four bytes to 
produce an output word."""
def SubWord():
    return

"""Function used in the Key Expansion routine that takes a four-byte 
word and performs a cyclic permutation. """
def RotWord():
    return



