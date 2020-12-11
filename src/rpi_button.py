import RPi.GPIO as GPIO

BUTTON_PIN = 4

def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def get_button_status():
	return GPIO.input(BUTTON_PIN)
	