from Character import Character

class Healer(Character):
  def __init__(self, name):
    super().__init__(name, 'Healer', hp=10, attack=5, defense=5, level=1, is_dead=False)