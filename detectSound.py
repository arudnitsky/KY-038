import RPi.GPIO as GPIO

MicPin = 3
LedPin = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(MicPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.LOW)

while False:
   input = GPIO.input(MicPin)
   print(input)
   GPIO.output(LedPin, input)
