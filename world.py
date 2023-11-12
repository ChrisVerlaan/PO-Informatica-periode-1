### Imports

from termcolor import colored

import time

import random

import sys

import os

from Functies import txt


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
				},
				"enemies":["Zwerver"],
				"objects" : ["deur"]
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
				"item": ["key"]
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
			txt("You see these enemies:")
			for monster in self.map[here]["monster"]:
				txt("  "+ str(monster)+ " : ", end="")
				txt(str(monster),"on encounter")
		#transitions
		txt("You see these doors:")
		for door in self.map[here]["transitions"]:
		 txt("  "+ str(door))
			#item
		if "items" in self.map[here]:
			txt("You see these items:")
			for item in self.map[here]["items"]:
				txt("  "+ str(item))
	
	
	
		 #
		print()
	
	
	def goto(self, direction): 
		if direction in self.map[self.here]["transitions"]:
		 txt("you walk " + str(direction) + "." )
		 self.here = self.map[self.here]["transitions"][direction]
		 return self.here
		else:
			txt("you can't go that way!")

	
	def removethingfromroom(world, item,typeofthing, thing, room=None):
		if room == None: room = world.here
			#check if anything is here
		if typeofthing in world.map[room]:
			# chekck if the thing is here
			if thing in world.map[room][typeofthing]:
				world.map[room][typeofthing].remove(thing)
			if len(world.map[room][typeofthing]) == 0:
				del world.map[room][typeofthing]
				return True
			else:
				return False
		else:# cant remove what is not teher
			return True


