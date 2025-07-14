import serial
import struct
import time

ser = serial.Serial('COM7', 115200)

data = [1.0,2.0,3.0,9.0]

while 1:
    time.sleep(0.5)
    ser.write(struct.pack('<4f', *data))
