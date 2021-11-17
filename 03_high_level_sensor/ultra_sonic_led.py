import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 4
ECHO_PIN = 14
LED_PIN = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(TRIGGER_PIN, True)
        time.sleep(0.00001) # 10us, 1us = 0.000001
        GPIO.output(TRIGGER_PIN, False)
    
        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()

        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()

        duration_time = stop - start
        distance = duration_time * 17160

        print('Distance : %.1fcm'% distance)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')