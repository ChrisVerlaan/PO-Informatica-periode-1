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

player.showinventory()
# world=World(10)
# world.showStatus(player,here)
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
