import ctypes
import pylibi2c
import array

# MCP4725 default address is 0x60, 7-bit?
# https://www.programiz.com/python-programming/methods/built-in/bytes
# https://pypi.org/project/pylibi2c/
# https://stackoverflow.com/questions/66254152/suppress-deprecation-in-python 

# To do:
# - how to write an int to the dac? the dac hookup guide says it takes ints
# - does dac have a iaddr? idts! if it doesn't, try i2c_ioctl_read/write function for read/write, set'iaddr_bytes=0.
# - Make a byte array that is immutable and contains a known message (all '1's?). Use debugger to check that the array is made correctly.
# read needs an int object but write needs a byte? why? how do you write an int?
# do the page thingies, delays, ignore NAKs have anything to do with it?
# - make a while loop that writes the contents of the byte array to i2c port
# - try writing to 0x0 and 0x60. Is there any difference?
# - can you read from 0x60 (i.e can you read from the DAC?)

# 5/13
# i2c.ioctlwrite and i2c.ioctlread both run with no errors thrown (other than dep warnings). read keeps giving x01. write doesn't generate observable signals
# commenting out "i2c.flags = pylibi2c.I2C_M_IGNORE_NAK " gives the output "i2c.flags = pylibi2c.I2C_M_IGNORE_NAK \n -1". What does the return value does the IOCTL write function mean?
# reference youtube vids
# The reason why you weren't getting errors from the ioctlwrite commands was because you were ignoring the NACK flags with i2c.flags = pylibi2c.I2C_M_IGNORE_NAK.

#15/5
# I2C Output from Jetson Nano works
# no output from DAC though. 
# Possible reasons:
# - i2c output is poorly formatted
# - dac is fried? doubt it, cuz dac is still being detected on I2C Bus 0



print("Code starting...\n")
# Open i2c device @/dev/i2c-0, addr 0x60.
i2c = pylibi2c.I2CDevice('/dev/i2c-0', 0x60)

# Open i2c device @/dev/i2c-0, addr 0x60, 16bits internal address
#i2c = pylibi2c.I2CDevice('/dev/i2c-0', 0x60, iaddr_bytes=2)

# Set delay
i2c.delay = 10

# Set page_bytes
i2c.page_bytes = 1024 # must be between 8 and 1024 otherwise function throws a fit

# Set flags
#i2c.flags = pylibi2c.I2C_M_IGNORE_NAK 

# Python2
#buf = bytes(bytearray(256))

# Python3
bi = bytes(0)

int = 5 

print("hi\n")

#Error here: 
# Write data to i2c, buf must be read-only type
#size = i2c.write(0x60, buf)

print("Writing to bus 0...\n")
i = 999

while i > 0:
    #size = i2c.ioctl_read(0x0, int)
    size = i2c.ioctl_write(0xFF, bi)
    print(size)
    i -= 1

# From i2c 0x0(internal address) read 256 bytes data, using ioctl_read.
#data = i2c.ioctl_read(0x0, 256)