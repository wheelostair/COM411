def display_ladder(steps):

  print("| |\n***\n" * steps)
  print("| |")
  
def create_ladder():
  print("How many steps are remaining?\n")
  steps = int(input())

  display_ladder(steps)

create_ladder()