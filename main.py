### Imports

from termcolor import colored

import time

import random

import sys

import os

from battle import Battle



### Standaard Variables


player_name = "J.P. Balkenende"
here = "Nederland"
europa = {
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


inventory = []

### Standaard Defs


def txt(text):
	for x in colored(text, "white"): # Prints the text in wit
		sys.stdout.write(x) 
		sys.stdout.flush()
		time.sleep(0.03) # Zit een tijd tussen van 0.03 voor elke letter
	print()
	return ""


### Classes

# Class voor de speler
class Player:
	level = 1
	xp = 0
	next_level_xp = 500
	hp = 50
	max_hp = 50
	name =""
	
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
			print("ouch! you take", damage, " damage")
	
			if self.hp<= 0 :
				print("You died")
			else:
					print("ouch! you take", final_damage, " damage")
					print("you have",self.hp,"hp left")
		else:
			print("your armor protects you. You have no damage")
	def heal(self,heal_amount):
		self.hp += heal_amount

		if self.hp > self.max_hp:
			self.hp = self.max_hp

			print("You healed for",heal_amount, "hp")
			print("you currently have", self.hp, "/", self.max_hp , "hp")
		
	def xp_gain(self, xp_amount):
		self.xp += xp_amount
		print("you have gained",xp_amount,"xp")

		if self.xp >= self.next_level_xp:
			self.level +=1
			self.xp -= self_level_xp
			
			self.next_level_xp = int(self.next_level_xp * 1.25)
			self.max_hp = int(self.max_hp * 1.2)
			self.hp = self.max_hp

			print ("you've reached level", self.level, )
			self.print_stats()
	def equip_item(self,item):
		if item.item_type == "weapon":
			self.weapon = item
		elif item.item_type == "armor":
			self.armor = item
			print_stats()
		
	def print_stats(self):
		print()
		print("#########################")
		print("##### player stats: #####")
		print("#########################")
		print()
		( "name:",self.name)
		print("level:",self.level)
		print("hp:", self.hp,"/",self.max_hp)
		print("xp:",self.hp,"/",self.next_level_xp)
		print("-------------------------")
		self.weapon.print_stats()
		self.armor.print_stats()
		print("#########################")

	def showinventory():
		if len(inventory) > 0:
			print("<--- inventory --->" )
			for item in inventory:
				print("  " + item)
		else: 
			print("Your inventory is empty.")

	



# Class voor items
class Item:
	item_type = None

	def __init__( self,item_level):
		self.item_level = item_level
	def print_stats(self):
		print(self.item_type, "level:",self.item_level)
		
	def addtoinventory(item):
		global inventory
		# pick up item  
		if type(item) == list: # mutltiple items
			inventory += item
		else: # one item
			inventory.append(item) 
		# clean up inventory


		inventory.sort()#alphabetical order
		print()
		showinventory()

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
		print(self.weapon_type,"damage:",self.min_damage, "-", self.max_damage)



# Class voor armor
class Armor(Item):
	def __init__(self,item_level):
		Item.__init__(self,item_level)
		self.item_type = "armor"
		self.defence = item_level *2

	def print_stats(self):
		Item.print_stats(self)
		print("defence:",self.defence)


# Class voor monsters in het algemeen
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
		print(self.monster_type, "attacks for ", damage, "damage")
		return damage

	def take_hit(self, damage):
		self.hp -= damage


		if self.hp > 0:
			print(self.monster_type, "has", self.hp, "hitpoints left.")
		else:
			print(self.monster_type, "was slain")
		
	def print_stats(self):
		print(self.monster_type, " - level", self.level)


		if self.hp > 0:
			print("HP:", self.hp, "/", self.max_hp)
		else:
			print("*dead*")


# Class voor wolven
class Wolf(Monster):

	def __init__(self, level):
		self.monster_type = "Wolf"
		self.level = level
		self.hp = self.max_hp = self.level * 15
		self.min_damage = self.level + 1
		self.max_damage = self.level * 3
		self.xp_value = 100 + self.level * 20


# Class voor Katholieke
class Katholieke(Monster):

	def __init__(self, level):  
		self.monster_type = "Katholieke"
		self.level = level
		self.hp = self.max_hp = self.level * 10
		self.min_damage = self.level + 1
		self.max_damage = self.level * 2
		self.xp_value = 100 + self.level * 20


# Class voor Zwerver
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
			print(self.monster_type, "makes a critical hit!")
			damage *= 2
			return damage

# Class voor Ijsbeer
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
		return damage
		if random.randint(1,100) <= self.crit_chance:
			print(self.monster_type, "makes a critical hit!")
			damage *= 2
			return damage

# Class voor battles
class Battle:

	def __init__(self,player):
		self.player = player
		self.difficulty = random.randint(1,4)
		self.monster_list = []
		self.xp_value = 0
		monster_types = ["Wolf", "Zwerver","Katholieke","Ijsbeer"]

		for i in range(self.difficulty):
			monster_choice = random.choice(monster_types)
			if monster_choice == "Wolf":
				self.monster_list.append(Wolf(self.player.level))   
			elif monster_choice == "Zwerver":
				self.monster_list.append(Zwerver(self.player.level))
			elif monster_choice == "Katholieke":
				self.monster_list.append(Katholieke(self.player.level))
			elif monster_choice == "Ijsbeer":
				self.monster_list.append(Ijsbeer(self.player.level))

			self.xp_value += self.monster_list[i].xp_value
	def showStatus(): 
		print()
		print("###############################")
		print()
		#
		print("You are in the "+ here+ ".")
		#enemies
		if "monster" in europa[here]:
			print ("You see these enemies:")
			for monster in europa[here]["monster"]:
				print("  "+ monster+ " : ", end="")
				talk(monster,"on encounter")
		#transitions
		print("You see these doors:")
		for door in europa[here]["transitions"]:
		 print("  "+ door)
			#item
		if "items" in europa[here]:
			print ("You see these items:")
			for item in europa[here]["items"]:
				print("  "+ item)



		 #
		print()

	def battle_stats(self):
		print("You are fighting:")

		for i in range(self.difficulty):
			MonsterNummer = i + 1
			print("Enemy " + str(MonsterNummer))
			self.monster_list[i].print_stats()
			print()

		print("########################")
		print()


	def generate_loot(self):
		loot = False
		if self.difficulty == 1:
			if random.randint(1,100) <= 25:
				loot = True
		elif self.difficulty == 2:
			if random.randint(1,100) <=40:
				loot = True
		elif self.difficulty == 3:
			if random.randint(1,100) <= 60:
				loot = True

		if loot == True:
			loot_list = ["Weapon","Armor"]
			loot_type = random.choice(loot_list)

			if loot_type == "Weapon":
				item = Weapon(random.randint(self.player.level,self.player.level + 1))
				print("Yay! The monsters drop a new wepon!")
			elif loot_type == "Armor":
				item = Armor(random.randint(self.player.level,self.player.level + 1))
				print("Shiny! The monsters drop an armor!")  

			item.print_stats()
			print()
			print("Your current stats are:")
			self.player.print_stats()
			print()

			choice = imput("Do you want to equiq the new item? (Y/N)")
			choice = choice.lower()


			item.print_stats()
			print()
			print("Your current stats are:")
			self.player.print_stats()
			print()

			choice = imput("Do you want to equiq the new item? (Y/N)")
			choice = choice.lower()

			if choice == "n":
				print("you leave the item on the ground and move on...")
			else:
				self.player.equip_item(item)
				print("You equip the new item monsters beware!")
		else:
			print("You look real hard, but the monsters drop nothing...")


	def monster_attack(self):
		for monster in self.monster_list:
			if monster.hp >0:
				monster_damage = monster.attack()
				self.player.take_hit(monster_damage)


	def player_attack(self):
		target = -1
		if len(self.monster_list) >1:
			max_target = len(self.monster_list)
			while target < 0 or target > max_target:
				target = int(input("Which monster would you like to attack? (1 - " + str(max_target) +")",))
				target -= 1 

		player_damage = self.player.attack()

		if self.monster_list[target].hp >0:
			self.monster_list[target].take_hit(player_damage)
		else:
			print("You hit the dead monster. it is still dead...")
	def player_heal(self):
		if random.randint(1,100) <= 40:
			heal_amount = random.randint(self.player.max_hp // 4 , self.player.max_hp // 3)
			self.player.heal(heal_amount)
		else:
			print("You tried to heal yourself, but the spell failed..")


	def player_run(self):
		if random.randint(1,100) <= 25:
			print("You ran away as fast as you could and you've lost the monster")
			return True
		else:
			print("You tried to run away, but the monster will not let you")
			return False


	def player_quit(self):
		print("You give up....")
		self.player.hp = 0


	def fight_battle(self):
		print()
		print("You are under attack")


		while True:
			print()
			print("######### BATTLE ROUND ##########")
			self.battle_stats()


			player_action = ""
			while player_action not in ["S","F", "H","R","Q"]:
				player_action = input("What will you do? (S)tats, (F)ight,(H)eal,(R)un,(Q)uit").upper()

			if player_action == "S":
				self.player.print_stats()

				print()

			elif player_action == "F":
				self.player_attack()



				monster_alive = 0
				for monster in self.monster_list:
					if monster.hp > 0:
						monster_alive += 1


					if monster_alive > 0:
						self.monster_attack()
					else:
						print("########################")
						print("####### YOU WON ########")
						print("########################")
						print('''                             .---'::'        `---.
														(::::::'              )
														|`-----._______.-----'|
														|              :::::::|
													 .|               ::::::!-.
													 \|               :::::/|/
														|               ::::::|
														|                    :|
														|                 ::::|
														|               ::::::|
														|              .::::::|
														J              :::::::F
														 \            :::::::/
															`.        .:::::::'
																`-._  .::::::-'
____________________________________|  """|"_________________________________________
																		|  :::|
																		F   ::J
																	 /     ::\                                        
															__.-'      :::`-.__
														 (_           ::::::_)
															 `"""---------"""'
''')

						self.player.xp_gain(self.xp_value)
						self.generate_loot()

						break
			elif player_action == "H":
				self.player_heal()
				print()
				self.monster_attack()


			elif player_action == "R":
				if self.player_run() == True:
					break
				else:
					self.monster_attack()

			elif player_action == "Q":
				self.player_quit()
				break
			if self.player.hp <= 0:
				print("###########################")
				print("#!!!!!!!!!!!!!!!!!!!!!!!!!#")
				print("#!!!!!!! YOU HAVE DIED !!!#")
				print("###########################")
				print('''       _____  _____
																<     `/     |
																 >          (
																|   _     _  |
																|  |_) | |_) |
																|  | \ | |   |
																|            |
								 ______.______%_|            |__________  _____
							 _/                                       \|     |
							|                  J.P Balkenende              <
							|_____.-._________              ____/|___________|
																|            |
																|            |
																|            |
																|            |
																|   _        <
																|__/         |
																 / `--.      |
															 %|            |%
													 |/.%%|          -< @%%%
													 `\%`@|     v      |@@%@%%    - mfj
												 .%%%@@@|%    |    % @@@%%@%%%%
										_.%%%%%%@@@@@@%%_/%\_%@@%%@@@@@@@%%%%%%''')
				break




### Gamecode


player = Player(player_name)
print()
txt("Doel = verover de hele wereld")
txt("Veel succes, " + player_name + ", heel Nederland rekent op je !!!!!")
print()
print('''       _,--',   _._.--._____
 .--.--';_'-.', ";_      _.,-'
.'--'.  _.'    {`'-;_ .-.>.'
			'-:_      )  / `' '=.
				) >     {_/,     /~)
				|/               `^ .''')
print()
print('''             _._                                        _._
			_.----|   |--------------------------------------|   |----._
	 .-'      |.-.|      |     ||   || | | | | | | |     |.-.|      '-.
 .'        __| |__     |C|S|G|/   \|P|R|O|D|U|C|T|    __| |__        '.
|         |o_| |_o|    |_|_|_|     |_|_|_|_|_|_|_|   |o_| |_o|         |
|         ||_ @ _||  _    _ ___ _  _  _  _  _  _  _  ||_ @ _||         |
|         |o_| |_o| |_ |/| | | |_ |_|| || ||_)| \|_  |o_| |_o|         |
 '.          | |    __||\|-| | |_ |_||_||-||\_|_/__|    | |          .'
	 '-._     |'-'|                                      |'-'|     _.-'
			 '----|_ _|--------------------------------------|_ _|----''')
print()
print()
txt('''Commands --> 
   go [directions]
	 get [item]
	 use [item] ''')
print()
print()
input (txt("Druk op enter om te beginnen..."))
## 
battle_count = 0
while player.hp>0:
	print()
	print("______")
	print()
	battle_count +=1
	txt("battle " + str(battle_count))

	battle = Battle(player)
	

	battle.fight_battle()

print()
print("You have fought",battle_count, "battles")
player.print_stats()
print()
print("Thanks for playing!")
