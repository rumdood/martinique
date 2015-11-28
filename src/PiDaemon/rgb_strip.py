import RPi.GPIO as GPIO

class rgb_strip(object):
	
	def __init__(self, pins, frequency):
		GPIO.setmode(GPIO.BCM)
		self.__pins = dict()
		
		for set_color, pin in pins.items():
			GPIO.setup(pin, GPIO.OUT)
			
		self.__pins['RED'] = GPIO.PWM(pins["red"], frequency)
		self.__pins['RED'].start(0)
		self.__pins['GREEN'] = GPIO.PWM(pins["green"], frequency)
		self.__pins['GREEN'].start(0)
		self.__pins['BLUE'] = GPIO.PWM(pins["blue"], frequency)
		self.__pins['BLUE'].start(0)
		
	def __enter__(self):
		return self
		
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.cleanup()
		return True
	
	def set_color(self, red, green, blue, post_delay):
		self.__pins['RED'].ChangeDutyCycle(red)
		self.__pins['GREEN'].ChangeDutyCycle(green)
		self.__pins['BLUE'].ChangeDutyCycle(blue)
		time.sleep(post_delay)
		
	def cleanup(self):
		for color, pin in self.__pins.items():
			pin.stop()
			
		GPIO.cleanup()