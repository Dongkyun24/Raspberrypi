import RPi.GPIO as GPIO

LED_PIN = 4
GPIO.setmode(GPIO.BCM) # 핀번호 체계를 GPIO로 설정
GPIO.setup(LED_PIN, GPIO.OUT) # LED_PIN(4번 핀)을 OUT모드로 변경

try:
    while True:
        val = input("1:on, 0:off, 9:exit >")
        if val == '0':
            GPIO.output(LED_PIN, GPIO.LOW) # LED OFF
            print("led off")
        elif val == '1':
            GPIO.output(LED_PIN, GPIO.HIGH) # LED ON
            print("led on")
        elif val == '9':
            break
finally:
    GPIO.cleanup() # 초기화
    print("cleanup and exit")



