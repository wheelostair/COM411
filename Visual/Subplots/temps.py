import matplotlib.pyplot as plt

def read_data(file_name):
  with open(file_name)as file:
    data = []
    for line in file:
      data.append(int(line.strip()))
    print(data)  
  #file.close()

  return data

def run():
  
  data = read_data("Visual/Subplots/temps.txt")

  fig, (ax1,ax2) = plt.subplots(1,2)
  y = data
  x = range(1,8,1)
  ax1.plot(x,y)
  ax1.set_ylim(15,25)
  ax1.set_xlim(1,7)
  ax2.bar(x,y)
  ax2.set_ylim(15,25)
  ax2.set_xlim(0,8)

  plt.tight_layout()
  plt.show()

run()