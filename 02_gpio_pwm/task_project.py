# 스위치로 LED 제어하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 8
SWITCH_PIN_1 = 12
SWITCH_PIN_2 = 13
SWITCH_PIN_3 = 14

GPIO.setmode(GPIO.BCM) # GPIO.BCM 핀번호 체계로 설정
GPIO.setup(SWITCH_PIN_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
GPIO.setup(SWITCH_PIN_2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
GPIO.setup(SWITCH_PIN_3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(80) # duty cycle (0~100) . 소리 크기

# 내부 풀다운 저항 pull_up_down = GPIO.PUD_DOWN

try:
    while True:
        val1 = GPIO.input(SWITCH_PIN_1) 
        val2 = GPIO.input(SWITCH_PIN_2) 
        val3 = GPIO.input(SWITCH_PIN_3) 
        if val1 == 1:
            pwm.ChangeFrequency(262)
        elif val2 == 1:
            pwm.ChangeFrequency(294)
        elif val3 == 1:
            pwm.ChangeFrequency(330)

finally:
    GPIO.cleanup()
    print('cleanup and exit')

            