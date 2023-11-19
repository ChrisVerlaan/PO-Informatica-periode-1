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

from world import World

class Battle:

	def __init__(self,player,enemies):
		self.player = player
		# self.difficulty = random.randint(1,4)
		self.monster_list = []
		self.xp_value = 0
		monster_types = ["Wolf", "Zwerver","Katholieke","Ijsbeer"]

		for i, monster_choice in enumerate(enemies):
			# monster_choice = random.choice(monster_types)
			if monster_choice == "Wolf":
				self.monster_list.append(Wolf(self.player.level))   
			elif monster_choice == "Zwerver":
				self.monster_list.append(Zwerver(self.player.level))
			elif monster_choice == "Katholieke":
				self.monster_list.append(Katholieke(self.player.level))
			elif monster_choice == "Ijsbeer":
				self.monster_list.append(Ijsbeer(self.player.level))

			self.xp_value += self.monster_list[i].xp_value


	def battle_stats(self,here):
		txt("Je bent aan het vechten:")
		# if "monster" in self.map[world.here]:
		# 	for monster in self.map[world.here]["monster"]:
		# 		txt("  "+ str(monster)+ " : ", end="")
		# 		txt("je komt een " + str(monster) + " tegen")
		# 		self.monster_list[i].print_stats()
		# 		print()
		# for i in range(self.difficulty):
		# 	MonsterNummer = i + 1
		# 	txt("Vijand " + str(MonsterNummer))
		# 	self.monster_list[i].print_stats()
		# 	print()

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
				txt("Joepie! Het monster heeft een nieuw wapen achtergelaten!")
			elif loot_type == "Armor":
				item = Armor(random.randint(self.player.level,self.player.level + 1))
				txt("Wauw! Het monster heeft armor achtergelaten!")  

			item.print_stats()
			print()
			txt("Jouw huidige statistieken zijn:")
			self.player.print_stats()
			print()


			choice = txt(input("Wil je je nieuwe voorwerp dragen? (Y/N)"))

			choice = choice.lower()


			item.print_stats()
			print()
			txt("Jouw huidige statistieken zijn:")
			self.player.print_stats()
			print()

			choice = txt(input("Wil je je nieuwe voorwerp dragen? (Y/N)"))
			choice = choice.lower()

			if choice == "n":
				txt("Je laat het voorwerp liggen en gaat verder....")
			else:
				self.player.equip_item(item)
				txt("Je draagt het nieuwe voorwerp; pas maar op monsters!")
		else:
			txt("Je kijkt grondig, maar je ziet niks liggen")


	# def fight_enemy(self):
	# 	for monster in self.monster_list:
	# 		if monster.hp >0:
	# 			monster_damage = monster.attack()
	# 			self.player.take_hit(monster_damage)
	def fight_enemy(self, enemy):
		if enemy in self.monster_list:
				target = self.monster_list.index(enemy)
				player_damage = self.player.attack()
				if self.monster_list[target].hp > 0:
						self.monster_list[target].take_hit(player_damage)
				else:
						txt("Je raakt het monster. Het is nog steeds dood.")

	def player_attack(self):
		target = -1
		if len(self.monster_list) >1:
			max_target = len(self.monster_list)
			while target < 0 or target > max_target:
				target = int(input("Welk monster wil je aanvallen? (1 - " + str(max_target) +")",))
				target -= 1 

		player_damage = self.player.attack()

		if self.monster_list[target].hp >0:
			self.monster_list[target].take_hit(player_damage)
		else:
			txt("Je raakt het monster. Hij is nog steeds dood.")
	def player_heal(self):
		if random.randint(1,100) <= 40:
			heal_amount = random.randint(self.player.max_hp // 4 , self.player.max_hp // 3)
			self.player.heal(heal_amount)
		else:
			txt("Je probeerde te healen, maar het mislukte...")


	def player_run(self):
		if random.randint(1,100) <= 25:
			txt("Je rent zo hard als je kan! Het monster is je kwijt.")
			return True
		else:
			txt("Je probeert weg te rennen, maar het mislukte.")
			return False


	def player_quit(self):
		txt("Je geeft op....")
		self.player.hp = 0


	def fight_battle(self,here):

		print()
		txt("Je wordt aangevallen")
		


		while True:
			print()
			txt("######### BATTLE ROUND ##########")
			self.battle_stats(world.here)


			player_action = ""
			while player_action not in ["S","F", "H","R","Q"]:
				player_action = input(txt("Wat ga je doen? (S)tats, (F)ight,(H)eal,(R)un,(Q)uit")).upper()

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
						self.fight_enemy()
					else:
						txt("#############################")
						txt("####### YOU killed it #######")
						txt("#############################")
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
				self.fight_enemy()


			elif player_action == "R":
				if self.player_run() == True:
					break
				else:
					self.fight_enemy()

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



