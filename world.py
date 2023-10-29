### Imports

from termcolor import colored

import time

import random

import sys

import os


class World():
	here = 0
	
	current_world = 
	
def goto(direction): 
	global here
	if direction in world[here]["transitions"]:
	 print("you walk " + direction + "." )
	 here = world[here]["transitions"] [direction]
	else:
		print("you can't go that way!")
		
class Europa(World):
	
	def __init__(self):
		self.here = "Nederland"
		self.map_name = europa
		self.map = {
			"Nederland": {
				"transitions": {
					"oosten" : "Duitsland",
					"zuiden" : "Frankrijk"
				},
			},
			"Duitsland" : {
				"transitions": {
					"westen": "Nederland",
					"noorden": "Scandinavie"

				},
			},
			"Frankrijk" : {
				"transitions": {
					"noorden": "Nederland",
					"westen" : "Engeland",
					"zuiden" : "Spanje"
				},
			},
			"Spanje" : {
				"transitions": {
					"noorden": "Frankrijk"

				},

			},

			"Engeland": {
				"transitions": {
					"oosten": "Frankrijk"

				},
			},
			"Scandinavie": {
				"transitions": {
					"zuiden" : "Duitsland"
				},
				 "item": ["Key"]
			},

		}
		