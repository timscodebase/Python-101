import os
from art import *


TITLE = text2art('''
  Welcome to
  Papi's Text
  Adventure!
''')

os.system('clear')
print(green | TITLE)

input('Press any key to continue...')

os.system('clear')

character = input('Choice your character type:\na) Wizard\nb) Warrior\nc) Cleric\nd) Thief\n\n')
while character not in ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D']:
  character = input(red |'Invalid character type. Please choice your character type:\na) Wizard\nb) Warrior\nc) Cleric\nd) Thief\n\n')
if character == 'a' or character == 'A':
  print(green | 'You are a Wizard')
elif character == 'b' or character == 'B':
  print(blue | 'You are a Warrior')
elif character == 'c' or character == 'C':
  print(pink | 'You are a Cleric')
elif character == 'd' or character == 'D':
  print(teal | 'You are a Thief')
else:
  print(red | 'Invalid character type')
