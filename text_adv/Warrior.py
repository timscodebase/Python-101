from Character import Character

class Warrior(Character):
  def __init__(self, name):
    super().__init__(name, "Warrior", 10, 5, 5, 1, False)