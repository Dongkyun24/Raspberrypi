import cv2
import RPi.GPIO as GPIO
import time
from lcd import drivers
import datetime
import picamera

GPIO.setmode(GPIO.BCM)

switch_pin = 5
display = drivers.Lcd() # lcd 
# buzzer_pin = 4
#camera = picamera.PiCamera() 

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# path = ''

# 스위치 눌렀을 때 1
try:
    while True:
        # now = datetime.datetime.now() # 현재 시간
        display.lcd_display_string("hello world", 1)
        check = GPIO.input(switch_pin)
        if(check == 1):
            print("hello world")
            # display.lcd_display_string(now.strftime("%x %X"), 1)
            # display.lcd_display_string("turn off", 2)
            time.sleep(2)
            break
finally:
    GPIO.cleanup()   
    display.lcd_clear()