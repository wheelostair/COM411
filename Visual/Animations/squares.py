import matplotlib.pyplot as plt   
import matplotlib.animation as animation

boxes = []

fig, ax = plt.subplots()

def init():
  small = {"x":(3,4,4,3,3),"y":(3,3,4,4,3)}
  medium = {"x":(2,5,5,2,2),"y": (2,2,5,5,2)}
  large = {"x":(1,6,6,1,1),"y": (1,1,6,6,1)}

  boxes.append(small)
  boxes.append(medium)
  boxes.append(large)
  
  return (boxes)

def animate(frame):
  data = init()
  x = data[0]
  y = data[1]

  print (data)
  ax.plot(x, y)

def run():
  global fig  
  simple_animation = animation.FuncAnimation(fig,animate, frames = 10, interval = 1000)

  plt.show()

run()