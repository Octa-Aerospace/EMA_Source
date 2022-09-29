import RPi.GPIO as GPIO
from time import sleep

class RGB:
    def __init__(self, redPin=12, greenPin=19, bluePin=13):
        self.redPin = redPin
        self.greenPin = greenPin
        self.bluePin = bluePin

    def turnOn(self, pin):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    def turnOff(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    def redOn(self):
        self.turnOn(self.redPin)

    def redOff(self):
        self.turnOff(self.redPin)

    def greenOn(self):
        self.turnOn(self.greenPin)

    def greenOff(self):
        self.turnOff(self.greenPin)

    def blueOn(self):
        self.turnOn(self.bluePin)

    def blueOff(self):
        self.turnOff(self.bluePin)

    def yellowOn(self):
        self.turnOn(self.redPin)
        self.turnOn(self.greenPin)

    def yellowOff(self):
        self.turnOff(self.redPin)
        self.turnOff(self.greenPin)

    def cyanOn(self):
        self.turnOn(self.greenPin)
        self.turnOn(self.bluePin)

    def cyanOff(self):
        self.turnOff(self.greenPin)
        self.turnOff(self.bluePin)

    def magentaOn(self):
        self.turnOn(self.redPin)
        self.turnOn(self.bluePin)

    def magentaOff(self):
        self.turnOff(self.redPin)
        self.turnOff(self.bluePin)

    def whiteOn(self):
        self.turnOn(self.redPin)
        self.turnOn(self.greenPin)
        self.turnOn(self.bluePin)

    def whiteOff(self):
        self.turnOff(self.redPin)
        self.turnOff(self.greenPin)
        self.turnOff(self.bluePin)

    def orangeOn(self):
        self.turnOn(self.redPin)
        self.yellowOn()

if __name__ == "__main__":
    LED = RGB()
    LED.redOn()
