#import GPIO and time libraries
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) #ignore any fault coming from GPIO pins

ledPin = 11 #initializing led pin or making GPIO pin 11 as output
buttonPin = 16 #initializing buttonPin or making GPIO pin 16 as input
GPIO.setmode(GPIO.BOARD) #setting mode of the pin to BOARD or BCM

GPIO.setup(ledPin, GPIO.OUTPUT) #setting GPIO pin 11 as output
GPIO.setup(buttonPin, GPIO.LOW) #initially turining off the led

#input is fed to GPIO pin, so to maintain standard voltage and manage current limit
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(buttonPin, FALLING) #waits for button to get pressed
    print("buttonPin Pressed")
    GPIO.output(ledPin, GPIO.HIGH)
    GPIO.wait_for_edge(buttonPin, RISING) #waits for the button to get released
    GPIO.output(ledPin, GPIO.LOW)
GPIO.cleanup() #clean up GPIO pin to default setting

m