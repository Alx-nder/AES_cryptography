Creating a cryptography program based on the Advanced Encryption Standard (AES) algorithm.

The AES consist of four basic operations that are repeated over N rounds. These three operations are ADDING, SUBSTITUTING, SHIFTING, and MIXING.


Padding is a way to encrypt messages of a size that the block cipher would not be able to decrypt otherwise; it is a convention between whoever encrypts and whoever decrypts. If your input messages always have a length which can be processed with your encryption mode (e.g. your messages always have a length multiple of 16) then you do not have to add padding -- as long as during decryption, you do not try to look for a padding when there is none. If some of your messages require padding, then you will have to add some sort of padding systematically, otherwise decryption will be ambiguous.
https://security.stackexchange.com/questions/29993/aes-cbc-padding-when-the-message-length-is-a-multiple-of-the-block-size?msclkid=b22c3d65bc1f11eca6f4488c29bff633 



first we break the inout into a string of multipole 16
then we reshape thaat list into a 4x4 matrix

This is a simple lookup table, so we can just make two matrix and a function that access a position. The way to map a byte to this S-Box is to take the fist most significant nibble as the row, and the least significant nibble as the columns