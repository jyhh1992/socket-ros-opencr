########################
#serial_write.py
########################
import time
import serial

ser = serial.Serial ("/dev/ttyACM0", 115200) #Open port with baud rate

if __name__ == '__main__':
    ser.write(0x31) #transmit data serially
    time.sleep(2)
    ser.write(0x32) #transmit data serially
    time.sleep(2)
    ser.write(0x33) #transmit data serially
    time.sleep(2)
    ser.write(0x34) #transmit data serially
    time.sleep(2)

