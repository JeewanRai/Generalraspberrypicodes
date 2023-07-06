#importing camera module and time module 
from picamera import PiCamera
from time import sleep

#camera object of the PiCamera class is created 
#camera object will store information of camera such as setting, resolution, other features.
#its helpful in controlling of the camera and its features like preview camera or stop camera
camera = PiCamera() #creating object of camera to utilize the features of camera modules

camera.start_preview()
sleep(3)
camera.capture('/home/jeewan/Desktop/Photos/image.jpg')
camera.stop_preview()