from termcolor import colored

import time

import random

import sys

import os

from Extra import Item

from Extra import Weapon

from Extra import Armor

from Functies import txt


class Monster():
	
	hp = 1
	max_hp = 1
	min_damage = 1
	max_damge = 1
	
	monster_type = None
	
	xp_value = 1
	
	def __init__(self, level):
		self.level = level
	
	
	def attack(self):
		damage = random.randint(self.min_damage,self.max_damage)
		txt(str(self.monster_type) +  " attacks for " + str(damage)+ " damage ")
		return damage
	
	def take_hit(self, damage):
		self.hp -= damage
	
	
		if self.hp > 0:
			txt(str(self.monster_type) +  " has "+  str(self.hp) + "hitpoints left.")
		else:
			txt(str(self.monster_type) + " was slain ")
	
	def print_stats(self):
		txt(str(self.monster_type)+ " - level "+ str(self.level))
	
	
		if self.hp > 0:
			txt("HP: " +str(self.hp) +  "/" +  str(self.max_hp))
		else:
			txt("*dead*")
	

class Wolf(Monster):

	def __init__(self, level):
		self.monster_type = "Wolf"
		self.level = level
		self.hp = self.max_hp = self.level * 15
		self.min_damage = self.level + 1
		self.max_damage = self.level * 3
		self.xp_value = 100 + self.level * 20

class Zwerver(Monster):

	def __init__(self, level):
		Monster.__init__(self,level)
	
		self.monster_type = "Zwerver"
		self.level = level
		self.hp = self.max_hp = self.level * 20
		self.min_damage = 1
		self.max_damage = self.level * 4
		self.xp_value = 100 + self.level * 20
		self.crit_chance = max(30,level * 10)
	
	def attack(self):
		damage = random.randint(self.min_damage, self.max_damage)
		return damage
		if random.randint(1,100) <= self.crit_chance:
			txt(str(self.monster_type) + " makes a critical hit! ")
			damage *= 2
			return damage
			
class Katholieke(Monster):

	def __init__(self, level):  
		self.monster_type = "Katholieke"
		self.level = level
		self.hp = self.max_hp = self.level * 10
		self.min_damage = self.level + 1
		self.max_damage = self.level * 2
		self.xp_value = 100 + self.level * 20
	
class Ijsbeer(Monster):

	def __init__(self, level):
		Monster.__init__(self,level)
	
		self.monster_type = "Ijsbeer"
		self.level = level
		self.hp = self.max_hp = self.level * 20
		self.min_damage = 1
		self.max_damage = self.level * 4
		self.xp_value = 100 + self.level * 20
		self.crit_chance = max(30,level * 10)
	
	def attack(self):
		damage = random.randint(self.min_damage, self.max_damage)
	
		if random.randint(1,100) <= self.crit_chance:
			txt(str(self.monster_type)+ " makes a critical hit! ")
			damage *= 2
	
		return damage