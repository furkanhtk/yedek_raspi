import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
while True:
    ser.write(0xAA)
    #received_data = ser.read()              #read serial port
    sleep(0.5)
    #data_left = ser.inWaiting()             #check for remaining byte
    #received_data += ser.read(data_left)
    #print (received_data)                   #print received data
    #ser.write(received_data)                #transmit data serially 
