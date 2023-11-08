### Imports

from termcolor import colored

import time

import random

import sys

import os

from Functies import txt

class World():
	here = 0
	
	def __init__(self, size):
		self.size = size
		self.map = {}
	
	def showStatus(self,player,here): 
		print()
		print("###############################")
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
		