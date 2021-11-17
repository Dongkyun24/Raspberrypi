import picamera
import time
import os

path = '/home/pi/src6/06_multimedia'

camera = picamera.PiCamera()

while True:
    a = int(input("photo:1, vedio:2, exit:9 > "))

    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3)
    camera.rotation = 180
    if a == 1:
        print("사진촬영")
        camera.capture('{}/{}.jpg'.format(path, time.strftime("%Y%m%d_%H%M%S")))
    elif a == 2:
        try:
            print("동영상촬영")
            camera.start_recording('{}/{}.h264'.format(path, time.strftime("%Y%m%d_%H%M%S")))
            input("press enter to stop recoding..")
        finally:
            camera.stop_recording()
    elif a == 9:
        exit()