import time
import spidev

bus = 0
device = 0
spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz = 500000
spi.mode = 0

msg = [0x01]

while True:
    spi.writebytes(msg)
    x = spi.readbytes(5)
    print("result {}".format(x))
    time.sleep(1)
