class Robot:

  laws = "Protect, Obey and Survive"

  def the_laws():
    print(Robot.laws)

  def __init__(self):

    self.name = "Robot"
    self.age = 0

  def display(self):
    print(f"I am {self.name}")




class Human:

  MAX_ENERGY = 100

  def __init__(self):

    self.name = "Human"
    self.age = 0
    self.energy = 100

  def display(self):
    print(f"I am {self.name} and I am {self.age} years old")

