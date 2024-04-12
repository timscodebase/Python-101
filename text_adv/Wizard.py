from Character import Character

class Wizard(Character):
  def __init__(self, name):
    super().__init__(name, 'Wizzard', hp=10, attack=5, defense=5, level=1, is_dead=False)

  def cast_spell(self):
    if self.mp > 0:
      self.mp -= 1
    print("Casting spell...")