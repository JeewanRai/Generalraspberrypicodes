#importing picamera and time modules
from picamera import PiCamera
from time import sleep

camera = PiCamera() #creat object of the class PiCamera

camera.start_preview() #for streaming live preview
camera.start_recording('/home/Desktop/Video/video.h264') #recording video and saving in the file path
sleep(4)
camera.stop_recording()
camera.stop_preview()