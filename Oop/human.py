class Human:

  MAX_ENERGY = 100

  def __init__(self, name = "Human", age = 0):

    self.name = name
    self.age = age
    self.energy = Human.MAX_ENERGY

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old and I have {self.energy} energy.'

  def grow(self):
    self.age += 1

  def eat(self,amount):
    potential_energy = self.energy + amount
    if (potential_energy > Human.MAX_ENERGY):
      self.energy = Human.MAX_ENERGY
      return potential_energy - self.energy
    else:
      self.energy = potential_energy
      return 0
      
  def move(self,distance):
    if Human.MAX_ENERGY > 1:
      self.energy -= distance

if (__name__ == "__main__"):

  human=Human()
  human.grow()
  human.eat(3)
  human.move(4)
  
  print(human)