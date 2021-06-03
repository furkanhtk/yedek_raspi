import time
import spidev

current_time = time.localtime()

f = open("log.txt", "w")


bus = 0
device = 1
spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz = 500000
spi.mode = 0

while True:
    
    try:
        x = spi.readbytes(5)
        f.write("{}.{}.{}---Result = {}\n".format(current_time[3],current_time[4],current_time[5],x))
        print("{}.{}.{}---Result = {}".format(current_time[3],current_time[4],current_time[5],x))
        current_time = time.localtime()
	input("Press Enter to continue...")
        #time.sleep(1)
    except KeyboardInterrupt:
        f.close()

