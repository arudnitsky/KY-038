#!/usr/bin/python3
import math
import sys
import time
import RPi.GPIO as GPIO

def ease_inout_quint(x):
    return 16 * math.pow(x, 5) if x < 0.5 else 1 - math.pow(-2 * x + 2, 5) / 2

def ease_in_expo(x):
    return 0 if x == 0 else math.pow(2, 10 * x - 10)

def ease_out_expo(x):
    return 1 if x == 1 else 1 - math.pow(2, -10 * x)

def ramp_down_led():
    for rampIndex in range(100, 0, -1):
        dutyCycle = int(ease_out_expo(rampIndex/100) * 100)
        pwm.ChangeDutyCycle(dutyCycle)
        time.sleep(0.001)
    pwm.ChangeDutyCycle(0)


if __name__ == '__main__':

    MIC_PIN = 3
    LED_PIN = 5

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(MIC_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
    pwm = GPIO.PWM(LED_PIN, 100)
    pwm.start(0)

    input = GPIO.input(MIC_PIN)
    try:
        while True:

            if input == 1:
                while input == 1:
                    pwm.ChangeDutyCycle(100)
                    inputAsStr = str(input)
                    sys.stdout.write("*")
                    input = GPIO.input(MIC_PIN)
                sys.stdout.write("\n")
                sys.stdout.flush()
                ramp_down_led()
            input = GPIO.input(MIC_PIN)

    except KeyboardInterrupt:
        print ("\r\n" + sys.argv[0] + " SIGINT received - exiting")
        pwm.stop()
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()
