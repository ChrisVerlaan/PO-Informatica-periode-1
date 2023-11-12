from termcolor import colored

import time

import random

import sys

import os

from Functies import txt

from Extra import Item

from Extra import Weapon

from Extra import Armor

from Functies import txt

class Player:
	level = 1
	xp = 0
	next_level_xp = 500
	hp = 50
	max_hp = 50
	name =""
	inventory = []

	def __init__ (self,name):
		self.name = name

		self.weapon = Weapon(1)
		self.armor = Armor(1)

	def attack(self):
		damage = self.level + random.randint(self.weapon.min_damage,self.weapon.max_damage)
		txt(self.name + " attacks hits " + self.weapon.weapon_type + " for " + str(damage) + " damage.")
		return damage

	def take_hit(self, damage):

		final_damage = damage - self.armor.defence
		if final_damage > 0:

			self.hp -= final_damage
			txt("ouch! you take " +  str(damage)+ " damage")

			if self.hp<= 0 :
				txt("You died")
			else:
					txt("ouch! you take " + str(final_damage) + " damage")
					txt("you have "+ str(self.hp) +" hp left")
		else:
			txt("your armor protects you. You have no damage")
	def heal(self,heal_amount):
		self.hp += heal_amount

		if self.hp > self.max_hp:
			self.hp = self.max_hp

			txt("You healed for"+ str(heal_amount) + "hp")
			txt("you currently have" + str(self.hp) + "/" + str(self.max_hp) + "hp")

	def xp_gain(self, xp_amount):
		self.xp += xp_amount
		txt("you have gained"+ str(xp_amount) + "xp")

		if self.xp >= self.next_level_xp:
			self.level +=1
			self.xp -= self_level_xp

			self.next_level_xp = int(self.next_level_xp * 1.25)
			self.max_hp = int(self.max_hp * 1.2)
			self.hp = self.max_hp

			txt ("you've reached level" + str(self.level))
			self.print_stats()
	def equip_item(self,item):
		if item.item_type == "weapon":
			self.weapon = item
		elif item.item_type == "armor":
			self.armor = item
			print_stats()

	def print_stats(self):
		print()
		txt("#########################")
		txt("##### player stats: #####")
		txt("#########################")
		print()
		txt( "name:"+ str(self.name))
		txt("level:"+ str(self.level))
		txt("hp:"+ str(self.hp) +"/"+ str(self.max_hp))
		txt("xp:"+ str(self.hp) + "/"+ str(self.next_level_xp))
		txt("-------------------------")
		self.weapon.print_stats()
		self.armor.print_stats()
		txt("#########################")

	def showinventory(self):
		if len(self.inventory) > 0:
			txt("<--- inventory --->" )
			for item in inventory:
				txt("  " + str(item))
		else: 
			txt("Your inventory is empty.")
			




		inventory.sort()#alphabetical order
		print()
		showinventory() 

