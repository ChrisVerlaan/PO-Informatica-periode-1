import random 

class Player:
	level = 1
	xp = 0
	next_lever_xp = 500
	hp = 50
	max_hp = 50
	name =""
	
	def __init__ (self,name):
		self.name = name

		self.weapon = Weapon(1)
		self.armor = Armor(1)
		
	def attack(self):
		damage = self.level + random.randint(self.weapon.min_damage,self.weapon.max_damage)
		print(self.name,"attacks stih",self.Weapon_type,"for",damage,"damage")
		return damage
		
	def take_hit(self, damage):

		final_damage= damage - self.ermor.defence
		if final_damage > 0:
			
			self.hp -= final_damage
			print("ouch! you take", damage, " damage")
	
			if self.hp<= 0 :
				print("You died")
			else:
					print("ouch! you take", final_damage, " damage")
					print("you have",self.hp,"hp left")
		else:
			print("your armor protects you. You have nog damage")
	def heal(heal,real_amount):
		self.hp += heal_amount

		if self.hp > self.max_hp:
			self.hp = self.max_hp

			print("You heald for",heal_amount, "hp")
			print("you cuuently have", self.hp, "/", self.max_hp , "hp")
		
	def xp_gain(self, xp_amount):
		self.xp += xp_amount
		print("you have gained",xp_amount,"xp")

		if self.xp >= slef.nexl_level_xp:
			self.level +=1
			self.xp -= self_level_xp
			
			self.next_level_xp = int(self.next_level_xp * 1.25)
			self.max_hp = int(self.max_hp * 1.2)
			self.hp = self.map_hp

			print ("you've reached level", self.level, )
			self.print_stats()
	def equip_item(self,item):
		if item.item_type == "weapon":
			self.Weapon = item
		elif item.item_type == "armor":
			self.armor = item
			print_stats()
		
	def print_stats(self):
		print()
		print("#########################")
		print("##### player stats: #####")
		print("#########################")
		print( "name:",self.name)
		print("level:".self.level)
		print("hp:", slef.hp,"/",slef.max_hp)
		print("xp:",slef.hp,"/",slef.next_level_xp)
		print("-------------------------")
		self.weapon.print_stats()
		self.armor.print_stats()
		print("#########################")
		
class Item:
	item_type = None

	def __init__( self,item_level):
		self.item_level = item_level
	def print_stats(self):
		print(self.item_type, "level:",self.item_level)

	
class Weapon(Item):
	def __init__ (self,item_level):
		Item.__init__ (self,item_level)
		
		self.weapon = "weapon"

		weapon_list = ["sword","axe"]
		self.weapon_type = random.choice(weapon_list)

		if self.weapon_type == "sword":
			self.min_damage = self.item_level * 2
			self.max_damage = self.item_level * 3
		elif self.weapon_type == "axe":
			self.min_damage = 1
			self.max_damage = self.item_level * 4
	def print_stats(self):
		item.print_stats(self)
		print(self.weapon_type,"damage:",self.min_damage, "-", self.max_damage)
		
class Armor(Item):
	def __init__(self,item_level):
		Item.__init__(self,item_level)
		self.item_type = "armor"
		self.defence = self.item_type *2

	def print_stats(self):
		item.print_stats(self)
		print("defence:",self.defence)

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

class Skeleton(Monster):

	def __init__(self, level):
		Monster.__init__(self,level)

		self.monster_type = "Skeleton"

		self.hp = self.max_hp = self.level * 15
		self.min_damage = self.level + 1
		self.max_damage = self.level * 3
		self.xp_value = 100 + self.level * 20
		
class Troll(Monster):
	
	def __init__(self, level):
		Monster.__init__(self,level)

		self.monster_type = "Troll"

		self.hp = self.max_hp = self.level * 20
		self.min_damage = 1
		self.max_damage = self.level * 4
		self.xp_value = 100 + self.level * 20

		self.crit_chance = max(30,level * 10)

	def attack(self):
		damage = random.randint(self.min_damage, self.max_damage)

		if random.randindt(1,100) <= self.crit_chance:
			print(self.monster_type, "makes a critical hit!")
			damage *= 2

class Battle:


	def __init__(self,player):
		self.player = player
		self.difficulty = random.randint(1,3)
		self.monster_list = [ ]
		self.xp_value = 0
		monster_types = ["Skeleton", "Troll"]
	
		for i in range(self.difficulty):
			monster_choice = random.choice(monster_types)
				
			if monster_choice == ["Skeleton"]:
				self.monster_list.append(Skeleton(self.player.level))
			elif monster_choice == "Troll":
				self.monster_list.append(Troll(self.player.level))
			
				self.xp_value += self.monster_list[i].xp_value
				
	def battle_stats(self):
		print("You are fighting:")

		for i in range(self.difficulty):
			print("Enemy",i+1)
			self.monster_list[i].print_stats()
			print()

		print("########################")
		print()

		
	def generate_loot(self):
		loot = False
		if self.difficulty == 1:
			if radom.randint(1,100) <= 25:
				loot = True
		elif self.difficulty == 2:
			if radom.randint(1,100) <=40:
				loot = True
		elif self.difficulty == 3:
			if radom.randint(1,100) <= 60:
				loot = True

		if loot == True:
			loot_list = ["Weapon","Armor"]
			loot_type = Random.choice(loot_list)

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
				print("You equip the new item Mosters beware!")
		else:
			print("You look real hard, but the mosters drop nothing...")
	def monster_attack(self):
		for moster in self.monster_list:
			if moster.hp >0:
				moster_damage = monster.attack()
				self.player.take_hit(moster_damage)
				
		
	def player_attack(self):
		if len(self.monster_list) >1:
			max_target = len(self.mosnter_list)
			target =-1 
			while target < 1 or target.max_target:
				target = int(input("Which moster would you like to attack? (1 - ",max_target))
				target =- 1 
		else:
			target = 0

			
		player_damage = self.player.attack()

		if self.monster_list[target].hp >0:
			self.monster_list[target].take_hit(player_damage)
		else:
			print("You hit the dead monster. it is still dead...")
	def player_heal(self):
		if rondom.randit(1,100) <= 40:
			heal_amount = random.randit(self.player.max_hp // 4, self.player.map_hp // 3)
			self.player.heal(heal_amount)
		else:
			print("You tried to heal yourself, but the spell failed..")
		
		
	def player_run(self):
		if rondom.randit(1,100) <= 25:
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
				self.player.print()
				
			elif player_action == "F":
				self.player_attack
				


				monster_alive = 0
				for monster in self.monster_list:
					if monster.hp > 0:
						monsters_alive += 1


					if monster_alive > 0:
						self.monster_attack()
					else:
						print("########################")
						print("####### YOU WON ########")
						print("########################")

						self.player.xp_gain(self.xp_value)
						self.generate_loot()

						break
			elif player_action == "H":
				self.player_heal()
				print()
				self.monster_atack()


			elif player_action == "R":
				if self.player_run() == True:
					break
				else:
					self.monster_attack()

			elif player_action -- "Q":
				self.player_quit()
				break
			if self.player.hp <= 0:
				print("###########################")
				print("#!!!!!!!!!!!!!!!!!!!!!!!!!#")
				print("#!!!!!!! YOU HAVE DIED !!!#")
				print("###########################")
				break

player_name = input("What's your name, noble hero?")
player = Player(player_name)

print()
print("Good luck noble", player_name, "everyone is couting on you")
input ("press enter to enter the dungeon")

battle_count = 0
while player.hp>0:
	print()
	print("_____")
	print()
	battle_count +=1
	print("battle",battle_count)

	battle = Battle(player)
	battle.fight_battle()

print()
print("You have fought",battle_count, "battles")
player,print_stats()
print()
print("Thanks for playing!")
