### Imports

from termcolor import colored

import time

import random

import sys

import os

from Functies import txt

from Player import Player

class World():
	here = 0
	
	def __init__(self, size):
		self.size = size
		self.map = {}
	
	def showStatus(self,here): 
		print()
		txt("###############################")
		print()
		#
		txt("You are in the "+ str(here) + ".")
		#enemies
		if "monster" in self.map[here]:
			txt("You see these enemies:")
			for monster in self.map[here]["monster"]:
				txt("  "+ str(monster)+ " : ", end="")
				txt(str(monster),"on encounter")
		#transitions
		txt("You see these doors:")
		for door in europa[here]["transitions"]:
		 txt("  "+ str(door))
			#item
		if "items" in europa[here]:
			txt("You see these items:")
			for item in europa[here]["items"]:
				txt("  "+ str(item))
	
	
	
		 #
		print()
	def goto(self,direction,here): 
		#global here
		if direction in world[here]["transitions"]:
		 txt("you walk " + str(direction) + "." )
		 here = world[here]["transitions"] [direction]
		else:
			txt("you can't go that way!")
		
class Europa(World):
	
	def __init__(self):
		self.here = "Nederland"
		self.map_name = europa
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
		