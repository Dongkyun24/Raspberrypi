from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN = 26
LED_PIN2 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("led2.html")
    

@app.route("/led/<op>")
def on(op):
    if op == "Won":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "LED ON"

    elif op == "Woff":
        GPIO.output(LED_PIN, GPIO.LOW)
        return "LED OFF"
    elif op == "Ron":
        GPIO.output(LED_PIN2, GPIO.HIGH)
        return "LED ON"

    elif op == "Roff":
        GPIO.output(LED_PIN2, GPIO.LOW)
        return "LED OFF"
    else:
        return "Error"
        

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()