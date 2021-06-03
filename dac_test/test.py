import spidev
import time
spi = spidev.SpiDev()

bus=0
device=0

spi.open(bus, device)

#spi.max_speed_hz = 500000
spi.mode = 0

to_send = [0xB800]


for x in range(10):
   spi.writebytes(to_send)
   time.sleep(1)



