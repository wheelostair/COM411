import matplotlib.pyplot as plt   
import matplotlib.animation as animation
import numpy as np
     
fig, ax = plt.subplots()
    
def animate(frame): 
  ax.set_xlim(0, 721)
  ax.set_ylim(-1, 2)
  x = np.arange(0, frame)
  y = np.sin(x * np.pi/180) 
  ax.plot(x, y)
  
     
def run():
  global fig  
  simple_animation = animation.FuncAnimation(fig,animate, frames = 720, interval = 100)

  plt.show()
      
run()  