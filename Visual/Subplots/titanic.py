import csv
import matplotlib.pyplot as plt


def read_data():
  data = {'survived':[],'sex':[], 'age':[], 'fare':[]}

  with open("Visual/Subplots/titanic.csv",)as csvfile:
    csv_reader = csv.reader(csvfile)

    header = next(csv_reader)

    for line in csv_reader:
      survived = header[1].strip()
      sex = header[5].strip()
      age = header[6].strip()
      fare = header[10].strip()

    if (survived != "" and sex != "" and age != "" and fare != ""):
      data['survived'].append(bool(int(survived)))

      if (int(sex) == 0):
        data['sex'].append('male')
      else:
        data['sex'].append('female')

      data['age'].append(float(age))
      data['fare'].append(round(float(fare), 2))
    
  print (data)
  return (data)

read_data()
#def run():
  #data = read_data()
  #x = data[age]
  #y = data[survived]
  #fig, (ax1, ax2,ax3,ax4) = plt.subplots(4,2,sharex='all')
  #ax1.plot(data[y,x])
  #ax2.plot(data[age])
  #ax3.plot(data[survived])
  #ax4.plot(data[fare])

  #plt.show()

#run()