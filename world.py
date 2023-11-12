### Imports

from termcolor import colored

import time

import random

import sys

import os

from Functies import txt

from Player import Player


class World():
	def __init__(self, size):
		self.size = size
		self.here = "Nederland"
		self.map = {
			"Nederland": {
				"transitions": {
					"oost" : "Duitsland",
					"zuid" : "Frankrijk"
				},
			},
			"Duitsland" : {
				"transitions": {
					"west": "Nederland",
					"noord": "Scandinavie"

				},
			},
			"Frankrijk" : {
				"transitions": {
					"noord": "Nederland",
					"west" : "Engeland",
					"zuid" : "Spanje"
				},
				"enemies":["Zwerver"]
			},
			"Spanje" : {
				"transitions": {
					"noord": "Frankrijk"

				},
				"enemies":["Katholieke"]

			},

			"Engeland": {
				"transitions": {
					"oost": "Frankrijk"

				},
				"enemies":["Wolf"] 
			},
			"Scandinavie": {
				"transitions": {
					"zuid" : "Duitsland"
				},
				"enemies":["Ijsbeer"],
				"item": ["Key"]
			},

		}
	
	def showStatus(self ,here): 
		print()
		txt("###############################")
		print()
		#
		txt("You are in the "+ str(here) + ".")
		#enemies
		if "monster" in self.map[here]:
			txt("Je ziet deze vijanden:")
			for monster in self.map[here]["monster"]:
				txt("  "+ str(monster)+ " : ", end="")
				txt(str(monster),"on encounter")
		#transitions
		txt("Je ziet deze paden:")
		for door in self.map[here]["transitions"]:
		 txt("  "+ str(door))
			#item
		if "items" in self.map[here]:
			txt("Je ziet deze voorwerpen:")
			for item in self.map[here]["items"]:
				txt("  "+ str(item))
	
	
	
		 #
		print()
	
	
	def goto(self, direction): 
		if direction in self.map[self.here]["transitions"]:
		 txt("Je loopt " + str(direction) + "." )
		 self.here = self.map[self.here]["transitions"][direction]
		 return self.here
		else:
			txt("Daar kan je niet naartoe!")
	