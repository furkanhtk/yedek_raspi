import time
import spidev

current_time = time.localtime()



bus = 0
device = 0
spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz = 500000
spi.mode = 0

#msg = [0b00000000,0b00000001,0b00000010,0b00000011]
msg = [0x01]

dbm = input("dBm:")

f=open("{}_dBm.txt".format(dbm),'w')
f_csv=open("{}_dBm.csv".format(dbm),'w')
while True:
  try:
     freq = input("Frequency:")
     for x in range(25):
        time.sleep(0.5)
        #reply = spi.xfer(msg)
        spi.writebytes(msg)
        reply = spi.readbytes(2)
        print(reply)
        #list  = spi.readbytes(2)
        result = reply[0] << 8 | reply[1]
        print("dBm:{} dBm  Frequency:{} GHz Result = {}-----{}".format(dbm,freq,result,reply))
        f.write("dBm:{} dBm  Frequency:{} GHz Result = {}-----{}\n".format(dbm,freq,result,reply))
        f_csv.write("{},{},{}\n".format(dbm,freq,result,reply))
        #current_time = time.localtime()
  except KeyboardInterrupt:
     f.close()
     f_csv.close()
     break
