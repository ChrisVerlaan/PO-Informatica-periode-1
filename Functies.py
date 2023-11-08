from termcolor import colored

import time

import random

import sys

import os


def txt(text):
	for x in colored(text, "white"): # Prints the text in wit
		sys.stdout.write(x) 
		sys.stdout.flush()
		time.sleep(0.03) # Zit een tijd tussen van 0.03 voor elke letter
	print()
	return ""


