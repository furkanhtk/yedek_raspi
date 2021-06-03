import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
enable_pin=18
coil_1_pin=4  #GPIO4,7th pin is activated
coil_2_pin=17 #GPIO17,11th pin is activated
coil_3_pin=27 #GPIO27,13th pin is activated
coil_4_pin=22 #GPIO22,15th pin is activated
GPIO.setup(enable_pin,GPIO.OUT)
GPIO.setup(coil_1_pin,GPIO.OUT) #set 7th as an output
GPIO.setup(coil_2_pin,GPIO.OUT) #set 11th as an output
GPIO.setup(coil_3_pin,GPIO.OUT) #set 13th as an output
GPIO.setup(coil_4_pin,GPIO.OUT) #set 15th as an output
GPIO.output(enable_pin,1)
def setStep(w1,w2,w3,w4):
    GPIO.output(coil_1_pin,w1)# Blue coil
    GPIO.output(coil_2_pin,w2)# Pink coil
    GPIO.output(coil_3_pin,w3)# Yellow coil
    GPIO.output(coil_4_pin,w4)# Orange coil
def forward(delay,steps):
    for i in range(0,steps):
        setStep(1,0,0,1) #0
        time.sleep(delay)
        setStep(1,0,0,0) #1
        time.sleep(delay)
        setStep(1,1,0,0) #2
        time.sleep(delay)
        setStep(0,1,0,0) #3
        time.sleep(delay)
        setStep(0,1,1,0) #4
        time.sleep(delay)
        setStep(0,0,1,0)#5
        time.sleep(delay)
        setStep(0,0,1,1) #6
        time.sleep(delay)
        setStep(0,0,0,1) #7
        time.sleep(delay)       
def backwards(delay,steps):
    for i in range(0,steps):
        setStep(0,0,0,1) #7
        time.sleep(delay) 
        setStep(0,0,1,1) #6
        time.sleep(delay)
        setStep(0,0,1,0) #5
        time.sleep(delay)
        setStep(0,1,1,0) #4
        time.sleep(delay)
        setStep(0,1,0,0) #3
        time.sleep(delay)
        setStep(1,1,0,0) #2
        time.sleep(delay)
        setStep(1,0,0,0) #1
        time.sleep(delay)
        setStep(1,0,0,1) #0
        time.sleep(delay)
while True:
    perAngle=float(0.703125) #360/512=0.703, the angle of the motor at the each step
    delay = input("The time duration that between the steps")
    angle=int(input("Enter the desired angle for the clockwise direction"))
    steps = int(angle/perAngle)
    forward(int(delay) /1000.0,int(steps))
    angle_reversed=int(input("Enter the desired angle for the counterclockwise direction"))
    steps_reversed=int(angle_reversed/perAngle)
    backwards(int(delay)/1000.0,int(steps_reversed))
    
        
