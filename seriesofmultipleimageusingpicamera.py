#importing picamera and time module
from picamera import PiCamera
from time import sleep

camera = PiCamera() #instanciated PiCamera object 

camera.start_preview()
for i in range(5): #taking seriece of 5 images
    sleep(4)
    camera.capture('/home/Desktop/Photos/image%s.jpg' %1) #storing image with different names
    camera.stop_preview()