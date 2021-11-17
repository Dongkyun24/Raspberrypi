import RPi.GPIO as GPIO
import time

LED_PIN_1 = 4
LED_PIN_2 = 5
LED_PIN_3 = 6

GPIO.setmode(GPIO.BCM)

def LED_LIGHT(LED):
    GPIO.setup(LED,GPIO.OUT)
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED,GPIO.LOW)
    time.sleep(1)


LED_LIGHT(LED_PIN_1)
LED_LIGHT(LED_PIN_2)
LED_LIGHT(LED_PIN_3)

GPIO.cleanup()

