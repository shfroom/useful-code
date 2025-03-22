from time import sleep
import sys

def scrollTxt(text):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		sleep(0.03)

scrollTxt("Hello, World")