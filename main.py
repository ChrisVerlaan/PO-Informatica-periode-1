### Imports

from termcolor import colored

import time

import random

import sys

import os

from Functies import txt

from Battle import Battle

from world import World

from monster import Monster

from monster import Ijsbeer

from monster import Katholieke

from monster import Wolf

from monster import Zwerver

from Player import Player

from Extra import Item






### Standaard Variables


player_name = "J.P. Balkenende"





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
#showStatus = Battle(self)

battle_count = 0 


world = World(10)
item = Item(0)




while player.hp>0:
	world.showStatus(world.here)
	action = input('>')
	action = action.lower().split(" ",1)
	if action[0] == "go":
		world.goto(action[1]) 
		player.showinventory()
	elif action[0] == "get":
		item.getitem(action[1], world, item)
		print(str(item.invitem))
		player.addtoinventory(player, str(item.invitem))
	elif action[0] == "use":
		item.useitem(player, action[1], world)
		
	elif action[0] == "stats":
		showinventory()
	
	else:
		txt("Dit kan niet.")
		
	if "enemies" in world.map[world.here]:
		print()
		txt("There is a bad thing in this room.")
		txt("He is attacking you")
		print("______")
		print()
		battle_count +=1
		txt("gevecht " + str(battle_count))
	
		battle = Battle(player)
		
	
		battle.fight_battle(world.here)
	
		
print()
print("Je hebt",battle_count, "keer gevochten")
player.print_stats()
print()
print("Bedankt voor het spelen!")
