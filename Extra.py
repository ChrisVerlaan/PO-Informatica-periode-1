from termcolor import colored

import time

import random

import sys

import os

from Functies import txt

from world import World


class Item():
	item_type = None
	invitem = " "

	def __init__( self,item_level):
		self.item_level = item_level
	def print_stats(self):
		txt(str(self.item_type) + "level: "+ str(self.item_level))

	
		
	def getitem(l, pitem, world, item):
		global invitem #groetjes gio
		
		#check wheter the item is actually here
		if "item" in world.map[world.here] and pitem in world.map[world.here]["item"]:
			print("you found a "+ pitem + ".")
				# and remove it from the room: 
			world.removethingfromroom(world, "item",pitem)
			item.invitem = pitem

		else:
			# the item isn't there
			if "objects" in world.map[world.here] and item in world.map[world.here]["objects"]:
				print("The "+ item + " is too heavy to be lifted.") 
			else: 
				print("you cant pick up what isn't there...")

	def useitem(l, player, item, world):
		if not item in player.inventory:
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
	
		if "objects" in world.map[world.here]:
			if target in world.map[world.here]["objects"]:
				if target == "deur":
					world.map[world.here]["transitions"]["zuid"] = "Spanje"
				else:
					txt("that is not a legal target.")
			else:
				txt("thats not here...")
	
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

# Class voor armor
class Armor(Item):
	def __init__(self,item_level):
		Item.__init__(self,item_level)
		self.item_type = "armor"
		self.defence = item_level *2

	def print_stats(self):
		Item.print_stats(self)
		txt("defence: " + str(self.defence))


