import os
from art import *
from Colors import *
from utils import create_character, greet


TITLE = text2art('''
  Welcome to
  Papi's Text
  Adventure!
''')

os.system('clear')
print(green | TITLE)

input('Press any key to continue...')

os.system('clear')

my_character = None
character = input('Choice your character type:\na) Wizard\nb) Warrior\nc) Cleric\nd) Thief\n\n')
while character not in ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D']:
  character = input(red |'Invalid character type. Please choice your character type:\na) Wizard\nb) Warrior\nc) Cleric\nd) Thief\n\n')

if character == 'a' or character == 'A':
  print(green | 'You are a Wizard')
  my_character = create_character('Wizard')
  greet(my_character.name, my_character.description)

elif character == 'b' or character == 'B':
  print(blue | 'You are a Warrior')
  my_character = create_character('Warrior')
  greet(my_character.name, my_character.description)

elif character == 'c' or character == 'C':
  print(pink | 'You are a Cleric')
  my_character = create_character('Cleric') 
  greet(my_character.name, my_character.description)

elif character == 'd' or character == 'D':
  print(teal | 'You are a Thief')
  my_character = create_character('Thief')
  greet(my_character.name, my_character.description)

else:
  print(red | 'Invalid character type')
