#importing GPIO and time libraries
import RPi.GPIO as GPIO
import time

pirPin = 7 #defining GPIO pin 7 is for pir sensor
GPIO.setmode(GPIO.BOARD) #definign GPIO pin as BCM or BOARD mode
GPIO.setmode(pirPin, GPIO.IN) #defining pin 7 as input 
count = 0 #initially count is assingned 0, since no motion detected; it used to determine number of motion

while True:
    input_state = GPIO.input(pirPin) #taling input form PIR
    if input_state == True: #investigate the conditon, it its true or false
        print("Motion Detected" +str(count))
        count +=1
        time.sleep(0.3)
GPIO.cleanup()
