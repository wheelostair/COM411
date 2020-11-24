import csv
import matplotlib.pyplot as plt

week_1 = None
week_2 = None

def read_data():
  global week_1, week_2
  with open("Visual/Subplots/temps.csv")as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    header = next(csv_reader)

    week_1 = header[0].strip()
    week_2 = header[1].strip()
      
    data = {
      week_1:[],
      week_2:[]
      }
    
    for row in csv_reader:
      data[week_1].append(row[0].strip())
      data[week_2].append(row[1].strip())
    return data
    

def run():
  data = read_data()

  fig, (ax1, ax2) = plt.subplots(2, 1, sharex='all')
  ax1.plot(data[week_1])
  ax2.plot(data[week_2])
  
  plt.tight_layout()
  plt.show()

run()
  