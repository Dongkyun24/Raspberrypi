# '도'음 출력 (262Hz)
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 (262)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # duty cycle (0~100) . 소리 크기

time.sleep(2)
pwm.ChangeDutyCycle(0) # 부저음 끄기

pwm.stop()
GPIO.cleanup()
print('cleanup and exit')

