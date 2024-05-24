import smbus2
import time
import keyboard


# Define I2C address of the device
DEVICE_ADDRESS = 0x60

# Create a smbus object
bus = smbus2.SMBus(0)  # 0 indicates /dev/i2c-0

# Set bus to default high by writing high to DAC register and EEPROM
message = [0x9E, 0xC0, 0x60, 0x9E, 0xC0]
bus.write_i2c_block_data(DEVICE_ADDRESS, 0x60, message)

# while loop to set high / low when there's an input, and escape key
while True:
    if keyboard.is_pressed('h'):  # for high output, writing only to DAC register
        message = [0x9E, 0xC0, 0x40, 0x9E, 0xC0]
        bus.write_i2c_block_data(DEVICE_ADDRESS, 0x40, message)
        print("Output is now high.")

    elif keyboard.is_pressed('l'): # for low output, writing only to DAC register
        message = [0x00, 0x00, 0x40, 0x00, 0x00]
        bus.write_i2c_block_data(DEVICE_ADDRESS, 0x40, message)
        print("Output is now low.")

    elif keyboard.is_pressed('e'):
        print("Exiting program...")
        break  # escape 

bus.close()