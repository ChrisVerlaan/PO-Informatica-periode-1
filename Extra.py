from termcolor import colored

import time

import random

import sys

import os

from Functies import txt



class Item():
	item_type = None

	def __init__( self,item_level):
		self.item_level = item_level
	def print_stats(self):
		txt(str(self.item_type) + "level: "+ str(self.item_level))


	def removethingfromroom(item,typeofthing, thing, room=None):
		if room == None: room = here
			#check if anything is here
		if typeofthing in world[room]:
			# chekck if the thing is here
			if thing in world[room][typeofthing]:
				world[room][typeofthing].remove(thing)
			if len(world[room][typeofthing]) == 0:
				del world[room][typeofthing]
				return True
			else:
				return False
		else:# cant remove what is not teher
			return True
			
	def addtoinventory(item):
		global inventory
		# pick up item  
		if type(item) == list: # mutltiple items
			inventory += item
		else: # one item
			inventory.append(item) 
		# clean up inventory
		def getitem(self,item):
			#check wheter the item is actually here
			if "items" in world[here] and item in world[here]["items"]:
				print("you found a "+ item + ".")
				addtoinventory(item)
				# and remove it from the room: 
				removethingfromroom("items",item)

			else:
				# the item isn't there
				if "objects" in world[here] and item in world[here]["objects"]:
					print("The "+ item + " is too heavy to be lifted.") 
				else: 
					print("you cant pick up what isn't there...")
# Class voor weapons
class Weapon(Item):
	def __init__ (self,item_level):
		Item.__init__ (self,item_level)

		self.item_type = "weapon"

		weapon_list = ["sword","axe"]
		self.weapon_type = random.choice(weapon_list)

		if self.weapon_type == "sword":
			self.min_damage = self.item_level * 2
			self.max_damage = self.item_level * 3
		elif self.weapon_type == "axe":
			self.min_damage = 1
			self.max_damage = self.item_level * 4
	def print_stats(self):
		Item.print_stats(self)
		txt(str(self.weapon_type) + "damage: "+ str(self.min_damage) + "-" + str(self.max_damage))
		
	def useitem(item):
		if not item in inventory:
			print("you can't use what you don't have...")
			return

		# what to use the item on
		print("on what or whom?")
		target = input("> ").lower()
		print()

		#chek whether the target is in the room
		#use on yourself
		if target in ["self","myself","me", "my","i"]:
		
			useitemonself(item)



# Class voor armor
class Armor(Item):
	def __init__(self,item_level):
		Item.__init__(self,item_level)
		self.item_type = "armor"
		self.defence = item_level *2

	def print_stats(self):
		Item.print_stats(self)
		txt("defence: " + str(self.defence))


