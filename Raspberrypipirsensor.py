#importing GPIO and time module
import RPi.GPIO as GPIO
import time

pirPin = 7 #defining pin number
ledPin = 11 #defining pin number and assigning to ledPin variable

GPIO.setmode(GPIO.BOARD) #defining GPIO pins as BOARD or BCM pins
GPIO.setup(pirPin, GPIO.IN) #defining pirPin is input pin
GPIO.setup(ledPin, GPIO.OUT) #defining ledPin is output pin

count = 0 #count variable defined to count number of time motion occured, initially assigned 0
previous_state = False #this variable assigned to to compare with previous and current state of the sensor 

try:
    while True:
        current_state = GPIO.input(pirPin) #checks wether there is signal coming from sensor
        if current_state and not previous_state: #compares previous state and current state are same
            GPIO.output(ledPin, GPIO.HIGH) #put on led if previous and current singal does not match
            count +=1 #increment by 1
            print('Motion Detected', count)
        elif not current_state and previous_state: #compares again current and previous state 
            GPIO.output(ledPin, GPIO.LOW) # put of led
            
            previous_state = current_state #updating the value of previous state with current state
            time.sleep(0.3)
except KeyboardInterrupt: #executed when user interrupted the program using Ctrl+C
    print("Programe interrupted")

except  Exception as e:
    print('Program interrupted by pressing e', str(e))

finally:
    GPIO.cleanup() 

