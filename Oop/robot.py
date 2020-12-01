class Robot:

  MAX_ENERGY = 100

  laws = "Protect, Obey and Survive"

  def __init__(self, name = "Robot", age = 0):

    self.name = name
    self.age = age
    self.energy =Robot.MAX_ENERGY

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

  def the_laws():
    print(Robot.laws)

  def grow(self):
    self.age += 1

  def eat(self,amount):
    if self.energy < Robot.MAX_ENERGY:
      self.energy += amount
    
  def move(self,amount):
    self.energy -= amount

if (__name__ == "__main__"):

  robot=Robot()
  
  robot.grow()
  print(robot)
  robot.move(10)
  print(robot)
  robot.eat(40)
  print(robot)
  Robot.the_laws()