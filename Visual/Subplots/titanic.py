import csv
import matplotlib.pyplot as plt

survived = None
sex  = None
age  = None
fare   = None

def read_data():
  global survived, sex, age, fare
  with open("Visual/Subplots/titanic.csv", newline='')as csvfile:
    csv_reader = csv.reader(csvfile)

    header = next(csv_reader)

    survived = header[1].strip()
    sex = header[4].strip()
    age = header[5].strip()
    fare = header[9].strip()

    data = {
      survived:[],
      sex:[],
      age:[],
      fare:[]
      }
    
    

    for row in csv_reader:
      data[survived].append(int(row[1].strip()))
      data[sex].append(str(row[4].strip()))
      if row[5]:
        data[age].append(float(row[5].strip()))
      data[fare].append(float(row[9].strip()))
  print (data)
  return (data)


def run():
  data = read_data()
  x = data[age]
  y = data[survived]
  fig, (ax1, ax2,ax3,ax4) = plt.subplots(4,2,sharex='all')
  ax1.plot(data[y,x])
  #ax2.plot(data[age])
  #ax3.plot(data[survived])
  #ax4.plot(data[fare])

  plt.show()

run()