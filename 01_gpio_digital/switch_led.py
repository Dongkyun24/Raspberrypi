# 스위치로 LED 제어하기
import RPi.GPIO as GPIO
import time

LED_PIN = 7
SWITCH_PIN = 12

GPIO.setmode(GPIO.BCM) # GPIO.BCM 핀번호 체계로 설정
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
# 내부 풀다운 저항 pull_up_down = GPIO.PUD_DOWN

try:
    while True:
        val = GPIO.input(SWITCH_PIN) # 누르지 X -- > 0 누르면 --> 1
        print(val)
        time.sleep(0.1)
        GPIO.output(LED_PIN, val)
finally:
    GPIO.cleanup()
    print('cleanup and exit')

