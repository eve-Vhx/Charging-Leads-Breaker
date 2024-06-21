import smbus2
import time
import keyboard

# Define I2C address of the device
DEVICE_ADDRESS = 0x64

# Create a smbus object
bus = smbus2.SMBus(1)  # 1 indicates /dev/i2c-1

# Set DAC output to default high by writing high to DAC register and DAC EEPROM
message = [0x00, 0x00, 0x60, 0x00, 0x00]
bus.write_i2c_block_data(DEVICE_ADDRESS, 0x60, message)
print("Circuit is open by default.")

# Loop to set high / low when there's an input, and escape key
while True:
    if keyboard.is_pressed('h'):  # for high output, writing only to DAC register
        message = [0xEC, 0x09, 0xEC]
        bus.write_i2c_block_data(DEVICE_ADDRESS, 0x09, message) # note: the exact value (0x9EC) of high output was chosen arbitrarily.
        print("Circuit is now closed.")

    elif keyboard.is_pressed('l'): # for low output, writing only to DAC register
        message = [0x00, 0x00, 0x00]
        bus.write_i2c_block_data(DEVICE_ADDRESS, 0x00, message)
        print("Circuit is now open.")

    elif keyboard.is_pressed('e'): # escape 
        print("Exiting program...")
        break

# Close the bus connection
bus.close()
