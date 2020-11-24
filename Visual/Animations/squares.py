import matplotlib.pyplot as plt   
import matplotlib.animation as animation

boxes = []

fig, ax = plt.subplots()

def init():
  boxes.append({"x":[3,4,4,3,3],"y":[3,3,4,4,3]})
  boxes.append({"x":[2,5,5,2,2],"y": [2,2,5,5,2]})
  boxes.append({"x":[1,6,6,1,1],"y": [1,1,6,6,1]})

  return (boxes)

def animate(frame):
  global ax
  index = frame % len(boxes)
  ax.cla()
  ax.set_xlim(0, 7)
  ax.set_ylim(0, 7)
  ax.plot(boxes[index]["x"],boxes[index]["y"])

def run():
  global fig  
  simple_animation = animation.FuncAnimation(fig,animate, frames = 100, interval = 100, init_func=init)

  plt.show()

run()