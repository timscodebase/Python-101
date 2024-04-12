from Thief import Thief
from Cleric import Cleric
from Warrior import Warrior
from Wizard import Wizard

def create_character(type):
  name = input('Name your character: ')

  if type == 'Wizard':
    return Wizard(name)
  elif type == 'Warrior':
    return Warrior(name)
  elif type == 'Cleric':
    return Thief(name)
  elif type == 'Thief':
    return Cleric(name)