import ctypes
import array

# Python2
#buf = bytes(bytearray(256))

# Python3
bi = bytes([0])
print("bi has value: ")
print(bi)

bi = bytes(0)
print("bi has value: ")
print(bi)

bi = bytes([255])
print("bi has value: ")
print(bi)

int = 5

#Error here: 
# Write data to i2c, buf must be read-only type
#size = i2c.write(0x60, buf)

print("Writing to bus 0...\n")
i = 999