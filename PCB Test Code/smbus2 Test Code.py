import smbus2
import time
import keyboard

# Define I2C address of the device
DEVICE_ADDRESS = 0x64

# Create a smbus object
bus = smbus2.SMBus(0)  # 0 indicates /dev/i2c-0

# set bus to default high. writing high to DAC register and EEPROM
message = [0x00, 0x00, 0x60, 0x00, 0x00]
bus.write_i2c_block_data(DEVICE_ADDRESS, 0x60, message)
print("Circuit is open by default.")

# while loop to set high / low when there's an input, and escape key
while True:
    if keyboard.is_pressed('h'):  # for high output, writing only to DAC register
        message = [0xEC, 0x09, 0xEC]
        bus.write_i2c_block_data(DEVICE_ADDRESS, 0x09, message)
        print("Circuit is now closed.")

    elif keyboard.is_pressed('l'): # for low output, writing only to DAC register
        message = [0x00, 0x00, 0x00]
        bus.write_i2c_block_data(DEVICE_ADDRESS, 0x00, message)
        print("Circuit is now open.")

    elif keyboard.is_pressed('e'):
        print("Exiting program...")
        break  # escape 

# Close the bus connection
bus.close()
