#importing GPIO library and time library
import RPi.GPIO as GPIO
import time

#setting up GPIO pins are BCM or BOARD Mode
GPIO.setmode(GPIO.BOARD)

#assigning variable with GPIO pin
ledPin = 11

#defining GPIO pin as input or output
GPIO.setup(ledPin, GPIO.OUT)

#taking input from user for number of time to blink led
number_blink = int(input("Enter number of time to make LED blink: ")) #will read as string if we dont use int

#turn on and off led
for i in range(0, number_blink):
    GPIO.output(11, 1)
    time.sleep(1)
    GPIO.output(11, 0)
    time.sleep(1)
GPIO.cleanup()

