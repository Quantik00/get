import RPi.GPIO as GPIO
#import time
GPIO.setmode(GPIO.BCM) #теперь gpio 21 стал PIN40
GPIO.setup(24, GPIO.IN)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.input(24))



