def display_ladder(steps):
  print("| |")
  print("***\n|  |" * steps)
  
  
def create_ladder():
  print("How many steps are remaining?")
  steps = int(input())

  display_ladder(steps)

create_ladder()