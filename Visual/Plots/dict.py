import matplotlib.pyplot as plt

import random as rnd

def data():
  paths = {}
  print(" What sort of line would you like (:, -- or -)?")
  line_style = input()
  
  print("What colour would you like (r, g or b)?")
  colour = input()
  
  print("What marker would you like (o, s or ^)?")
  marker_style = input()
  
  paths['line_style'] = line_style
  paths['colour'] = colour
  paths['marker_style'] = marker_style

  return paths

def generate():
  print("How many lines would you like to display?")
  lines = int(input())

  for line in range(lines):
    values = data()
    x = rnd.sample(range(1,10),5)
    y = rnd.sample(range(1,10),5)

    formatted = f"{values['colour']}{values['line_style']}{values['marker_style']}"

    print(formatted)
    plt.plot(x, y, formatted)
    
  

def run():
  print("Running...")
  generate()
  print("Done!")
  plt.show()

run()