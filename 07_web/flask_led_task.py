from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 4
LED_PIN2 = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

app = Flask(__name__)

@app.route("/")

def hello():
    return '''
    <p>Hello, Flask!!</p>
    <a href="/led/Won">Yellow Led On!</a>
    <a href="/led/Woff">Yellow Led Off!</a>
    <a href="/led/Ron">Blue Led On!</a>
    <a href="/led/Roff">Blue Led Off!</a>
    '''

@app.route("/led/<op>")

def on(op):
    if op == "Won":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
        <p>Led on</p>
        <a href="/">Go Home</a>
        '''
    elif op == "Woff":
        GPIO.output(LED_PIN, GPIO.LOW)
        return '''
        <p>Led off</p>
        <a href="/">Go Home</a>
        '''
    elif op == "Ron":
        GPIO.output(LED_PIN2, GPIO.HIGH)
        return '''
        <p>Led on</p>
        <a href="/">Go Home</a>
        '''
    elif op == "Roff":
        GPIO.output(LED_PIN2, GPIO.LOW)
        return '''
        <p>Led off</p>
        <a href="/">Go Home</a>
        '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:    
        GPIO.cleanup()
        print('cleanup and exit')