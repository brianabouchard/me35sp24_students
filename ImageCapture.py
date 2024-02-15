#import libraries 
from picamera2 import Picamera2 
import cv2 as cv 
from libcamera import controls
import time

picam2 = Picamera2()

#configure the picamera
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous}) #sets auto focus mode

picam2.start() #must start the camera before taking any images
time.sleep(1)

img_name = 'image.jpg'
picam2.capture_file(img_name) #take image 

picam2.stop() #stop the picam 
