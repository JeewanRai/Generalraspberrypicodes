#importing GPIO and time libraries
import RPi.GPIO as GPIO
import time

buttonPin = 16 #initializing button from where the input will be drawn

GPIO.setmode(GPIO.BOARD) #GPIO to BOARD mode, similar to physical pin

# pull up and down resistor are used for drawing in singnal from peripheral sensors to allow to draw 3.3V or 5V 
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) 

while True: #infinite loop
    input_state = GPIO.input(buttonPin) #taking reading from the button pin
    if buttonPin == False: # used pull up reistor, it will be TRUE when you press button
        print('Button Pressed')
        time.sleep(0.3) #to avoid bouncing, electronic concept delay is used.
GPIO.cleanup();
