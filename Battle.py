### Imports

from termcolor import colored

import time

import random

import sys

import os

from Functies import txt

from monster import Monster

from monster import Ijsbeer

from monster import Katholieke

from monster import Wolf

from monster import Zwerver

from Extra import Item

from Extra import Weapon

from Extra import Armor

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


	def battle_stats(self):
		txt("You are fighting:")

		for i in range(self.difficulty):
			MonsterNummer = i + 1
			txt("Enemy " + str(MonsterNummer))
			self.monster_list[i].print_stats()
			print()

		txt("########################")
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
				txt("Yay! The monsters drop a new wepon!")
			elif loot_type == "Armor":
				item = Armor(random.randint(self.player.level,self.player.level + 1))
				txt("Shiny! The monsters drop an armor!")  

			item.print_stats()
			print()
			txt("Your current stats are:")
			self.player.print_stats()
			print()

			choice = xtx (imput("Do you want to equiq the new item? (Y/N)"))
			choice = choice.lower()


			item.print_stats()
			print()
			xtx("Your current stats are:")
			self.player.print_stats()
			print()

			choice = xtx(imput("Do you want to equiq the new item? (Y/N)"))
			choice = choice.lower()

			if choice == "n":
				txt("you leave the item on the ground and move on...")
			else:
				self.player.equip_item(item)
				txt("You equip the new item monsters beware!")
		else:
			txt("You look real hard, but the monsters drop nothing...")


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
			txt("You hit the dead monster. it is still dead...")
	def player_heal(self):
		if random.randint(1,100) <= 40:
			heal_amount = random.randint(self.player.max_hp // 4 , self.player.max_hp // 3)
			self.player.heal(heal_amount)
		else:
			txt("You tried to heal yourself, but the spell failed..")


	def player_run(self):
		if random.randint(1,100) <= 25:
			txt("You ran away as fast as you could and you've lost the monster")
			return True
		else:
			txt("You tried to run away, but the monster will not let you")
			return False


	def player_quit(self):
		txt("You give up....")
		self.player.hp = 0


	def fight_battle(self):
		print()
		txt("You are under attack")


		while True:
			print()
			txt("######### BATTLE ROUND ##########")
			self.battle_stats()


			player_action = ""
			while player_action not in ["S","F", "H","R","Q"]:
				player_action = input(txt("What will you do? (S)tats, (F)ight,(H)eal,(R)un,(Q)uit")).upper()

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
						txt("########################")
						txt("####### YOU WON ########")
						txt("########################")
						txt('''                             .---'::'        `---.
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
				txt("###########################")
				txt("#!!!!!!!!!!!!!!!!!!!!!!!!!#")
				txt("#!!!!!!! YOU HAVE DIED !!!#")
				txt("###########################")
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



