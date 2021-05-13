# Python Class 2710
# Lesson 6 Problem 5
# Author: isaiah08 (595367)

import random
import time
### Die class that we previously wrote ###

class Die:
    '''Die class'''

    def __init__(self,sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides,int):
            self.numSides = sides
            self.sides = list(range(1,sides+1))
        else:  # use the list/tuple provided 
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A '+str(self.numSides)+'-sided die with '+str(self.get_top())+' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

### end Die class ###

class DinoDie(Die):
	'''implements one die for Dino Hunt'''
	def __init__(self, color):
		color_to_sides = {'green' : ['dino','dino','dino','leaf','leaf','foot'], 'yellow':['dino','dino','leaf','leaf','foot','foot'], 'red':['dino','leaf','leaf','foot','foot','foot']}
		self.color = color
		self.sides = color_to_sides[color]
		self.numSides = 6

        
        
    
class DinoPlayer:
	'''implements a player of Dino Hunt'''
	def __init__(self, name):
		self.score = 0
		self.name = name
	def turn(self):
		print(self.name + ', it is your turn!')
		time.sleep(.5)
		print('')
		dice = ['green','green','green','green','green','green','yellow','yellow','yellow','yellow','red','red','red']
		continue_turn = True
		feet = 0
		this_turns_score = 0
		while continue_turn == True:
			print('You have ' + str(len(dice)) + ' dice remaining.')
			if len(dice) > 2:
				dice_picked = random.sample(dice, 3)
				del dice[dice.index(dice_picked[0])]
				del dice[dice.index(dice_picked[1])]
				del dice[dice.index(dice_picked[2])]

				die1 = DinoDie(dice_picked[0])
				die2 = DinoDie(dice_picked[1])
				die3 = DinoDie(dice_picked[2])
				die1.roll()
				die2.roll()
				die3.roll()
				print('You rolled: ')
				print(die1)
				print(die2)
				print(die3)
				for x in [die1, die2, die3]:
					if x.get_top() == 'leaf':
						dice.append(x.color)
					elif x.get_top() == 'dino':
						this_turns_score += 1
					elif x.get_top() == 'foot':
						feet += 1
				if feet > 3:
					print('')
					print('You got STOMPED!!!')
					this_turns_score = 0
					break
				print('')
				print('You have ' + str(this_turns_score) + ' dinos and ' + str(feet) + ' feet.')
				print('Do you want to continue? y/n')
				contin = input('')
				if contin == 'y': continue_turn = True
				elif contin == 'n': 
					continue_turn = False 
					self.score += this_turns_score
			if len(dice) == 1:
				print('You roll 1 die.')
				die = DinoDie(dice[0])
				die.roll()
				print(die)
				if die == 'leaf':
					dice.append(die.color)
				elif die == 'dino':
					this_turns_score += 1
				elif die == 'foot':
					feet += 1
			

				if feet > 3:
					print('')
					print('You got STOMPED!!!')
					this_turns_score = 0
					break
				self.score += this_turns_score
				if len(dice) == 0:
					self.score += continue_turn
					continue_turn = False  
			elif len(dice) == 2:
				print('You roll 2 die.')
				die1 = DinoDie(dice[0])
				die2 = DinoDie(dice[1])
				die1.roll()
				die2.roll()
				print('A ' + die.color + ' die with a ' + die)
				for die in [die1, die2]:
					if die == 'leaf':
						dice.append(die.color)
					elif die == 'dino':
						this_turns_score += 1
					elif die == 'foot':
						feet += 1
			

				if feet > 3:
					print('')
					print('You got STOMPED!!!')
					this_turns_score = 0
					break
				self.score += this_turns_score
				if len(dice) == 0:
					self.score += continue_turn
					continue_turn = False  
			elif len(dice) == 0:
				break



					
            
            
        
        
        


   
def play_dino_hunt(numPlayers,numRounds):
	'''play_dino_hunt(numPlayer,numRounds)
	plays a game of Dino Hunt
	numPlayers is the number of players
	numRounds is the number of turns per player'''


	player_names = []
	player_accounts = []
	for i in range(1, numPlayers+1):
		player_name = input('Player ' + str(i)+', what is your name? ').title()
		player_names.append(player_name)
		player_accounts.append(DinoPlayer(player_name))


	for i in range(1, numRounds+1):
		print(('ROUND ' + str(i)).center(50, '-'))

		for x in range(0, numPlayers):
			player_accounts[x].turn()
			print('\n\n')
			print(player_names[x].title() + ' has '+ str(player_accounts[x].score)+ ' points.')
	print('GAME OVER'.center(50, '-'))

    
play_dino_hunt(2, 2)

