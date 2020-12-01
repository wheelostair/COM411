import random
import matplotlib.pyplot as plt
from human import Human
from robot import Robot
from planet import Planet

class Universe:

  def __init__(self):
    self.planets = {
      "humans" :[],
      "robots" :[]
      }

  def __repr__(self):
    return f"universe(planets={self.planets})"

  def __str__(self):
    return f'The universe has {len(self.planets)} planets, with {len(self.planets["humans"])} humans and {len(self.planets["robots"])} robots'

  def generate(self):
    planet = Planet()

    for index in range(random.randint(1,10)):
      robot = Robot(f"Robot{index}")
      self.planets["humans"].append(robot)
      

    for index in range(random.randint(1,10)):
      human = Human(f"Human{index}")
      self.planets["robots"].append(human)

    return [human,robot]
      
  

if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  print(universe)

  def show_pop():
    values = generate()
    fig, ax1 = plt.subplots(1,1)
    ax1.plot (values["humans"],values["robots"])
    

  plt.show()

  show_pop()