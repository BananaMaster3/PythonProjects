import time
import random
from os import system

def clear():
	system('clear')

def configure():
	masks = 0
	interactions = 0
	names = ['Jill','Bob','Marty']
	name = input("What is your name? ")
	print(f"""Hello {name}, welcome to
  _____         _    __  ___  ___ ______________   ____  ______
 / ___/__ _  __(_)__/ / / _ )/ _ /_  __/_  __/ /  / __/ / / / /
/ /__/ _ \ |/ / / _  / / _  / __ |/ /   / / / /__/ _/  /_/_/_/ 
\___/\___/___/_/\_,_/ /____/_/ |_/_/   /_/ /____/___/ (_|_|_)  
															   """)
	time.sleep(1)
	money = 10
	day = 1
	house(name,masks,interactions,names,money,day)

def house(name,masks,interactions,names,money,day):
	if day != 1:
		day += 1
	
	clear()
	covid_chance = interactions-masks
	if covid_chance > 100:
		print('''
  __  ____     ____  __   __  __  ______  __  __  ___  ___________    __
 / / / / /    / __ \/ /  / /  \ \/ / __ \/ / / / / _ \/  _/ __/ _ \  / /
/ /_/ / _ \  / /_/ / _ \/_/    \  / /_/ / /_/ / / // // // _// // / /_/ 
\____/_//_/  \____/_//_(_)     /_/\____/\____/ /____/___/___/____/ (_)  
																		
''')
	elif day == 10:
		print('''
  _____                        __      __  __  __                          __      _ __    __                __                       _ __  __             __       __     _             __
 / ___/__  ___  ___ ________ _/ /____ / /  \ \/ /__  __ __  __ _  ___ ____/ /__   (_) /_  / /____ ___    ___/ /__ ___ _____   _    __(_) /_/ /  ___  __ __/ /_  ___/ /_ __(_)__  ___ _  / /
/ /__/ _ \/ _ \/ _ `/ __/ _ `/ __(_-</_/    \  / _ \/ // / /  ' \/ _ `/ _  / -_) / / __/ / __/ -_) _ \  / _  / _ `/ // (_-<  | |/|/ / / __/ _ \/ _ \/ // / __/ / _  / // / / _ \/ _ `/ /_/ 
\___/\___/_//_/\_, /_/  \_,_/\__/___(_)     /_/\___/\_,_/ /_/_/_/\_,_/\_,_/\__/ /_/\__/  \__/\__/_//_/  \_,_/\_,_/\_, /___/  |__,__/_/\__/_//_/\___/\_,_/\__/  \_,_/\_, /_/_//_/\_, / (_)  
			  /___/                                                                                              /___/                                             /___/       /___/       
''')
	else:
		print(f"You are in your house. You have {masks} masks, and a {(covid_chance)}% chance of getting covid. What would you like to do: \n[1] Go online\n[2] Go to the library\n[3] Take a walk\n[4] Go to someone's house")
		choice = input("Please choose 1, 2, 3, or 4.")
		if choice == '1':
			activities.online(name,masks,interactions,names,money,day)
		elif choice == '2':
			activities.library(name,masks,interactions,names,money,day)
		elif choice == '3':
			activities.walk(name,masks,interactions,names,money,day)
		elif choice == '4':
			activities.visit_a_house(name,masks,interactions,names,money,day)

class activities():
	def visit_a_house(name,masks,interactions,names,money,day):
		print(f"You visit your freind {random.choice(names)}'s house.")
		interactions += 2
		time.sleep(3)
		house(name,masks,interactions,names,money,day)
	def online(name,masks,interactions,names,money,day):
		clear()
		print("You have opened your computer, and you are on the web. Please select an option:\n[0] Exit\n[1] Skype\n[2] Amazon\n[3] News")
		choice = input("Please choose 1, 2, 3, or 4. ")
		if choice == '0':
			print(f"END OF DAY {day} \n")
			time.sleep(2.5)
			house(name,masks,interactions,names,money,day)
		
		elif choice == '1':
			clear()
			random.shuffle(names)
			print("You talk to your good friend " + names[0] + ".\n\n")
			print(f"END OF DAY {day} \n")
			time.sleep(2.5)
			house(name,masks,interactions,names,money,day)

		elif choice == '2':
			print("You go on amazon and can buy the following items:\n[0] Exit (not an item)\n[1] Masks\n[2] That's all! (also not an item)")
			
			choice = input("Please choose 0 or 1. ")
			if choice == '0':
				print(f"END OF DAY {day} \n")
				time.sleep(2.5)
				house(name,masks,interactions,names,money,day)
			elif choice == '1':
				masks += 10
				print("You buy 10 masks and have more money left.")
				money = 0
				print(f"END OF DAY {day} \n")
				time.sleep(2.5)
				house(name,masks,interactions,names,money,day)
		elif choice == '3':
                    print("You read about the horrible things that are happening in the US. You feel so bad that you go to sleep imediately.")
                    print(f"END OF DAY {day} \n")
                    time.sleep(2.5)
                    house(name, masks, interactions,names,money,day)
                    

	def library(name,masks,interactions,names,money,day):
		interactions += random.randint(1,5)
		print("Go to the library and check out some books. ")
		print(f"END OF DAY {day} \n")
		time.sleep(2.5)
		house(name,masks,interactions,names,money,day)
	def walk(name,masks,interactions,names,money,day):
		print("As you go on your walk, you see someone coming torward you. Do you:\n[1] Avoid, stay six feet away\n[2] Come close")
		choice = input("Please choose 1 or 2. ")
		if choice == '1':
			print("You stay far away. ")
			print(f"END OF DAY {day} \n")
			time.sleep(2.5)			
			house(name,masks,interactions,names,money,day)
		elif choice == '2':
			safety = random.randint(0,1)
			if safety == '0':
				print("Even though you continue walking, the other person crosses the street to avoid you.")
				print(f"END OF DAY {day} \n")
				time.sleep(2.5)
				house(name,masks,interactions,names,money,day)

			else:
				print("You walk right by the person. ")
				interactions += 20
				print(f"END OF DAY {day} \n")
				time.sleep(2.5)
				house(name,masks,interactions,names,money,day)
				

clear()
configure()
