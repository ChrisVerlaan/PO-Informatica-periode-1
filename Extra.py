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


