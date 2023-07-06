#importing Raspberry Pi GPIO and time module/library for control
import RPi.GPIO as GPIO
import time

#to supress any kind of warning generated by GPIO library, we use following code to keep output clean
GPIO.setwarnings(False)

#defininig the pin of the LED where it should be connected, initilizing the led pin
ledPin = 11

GPIO.setmode(GPIO.BOARD) #defining GPIO mode to BCM or BOARD mode

GPIO.setup(ledPin, GPIO.OUT) #defining the pin as input or output
GPIO.output(ledPin, GPIO.HIGH) #initially keeping led on 

while True: #for continuous putting on and off led light
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(1) #delay for 1sec
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup() #cleaning up the GPIO pin once exit



