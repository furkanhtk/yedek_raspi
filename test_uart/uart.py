import time
import serial

ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1000
)

data='4000000000,2048'

while 1:
    try:
        ser.write(str(data).encode())
        time.sleep(1)
    except KeyboardInterrupt:
        ser.close()
