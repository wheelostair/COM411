def sum_weights(beep,bop):
  total_weight = (beep + bop)
  return print("The sum of Beep and Bops weight is",total_weight)

def calc_avg_weight(beep,bop):
  avg_weight = (beep + bop) /2
  return print("The average of Beep and Bops weight is",avg_weight)
  

def run():
  print("What is the weight of Beep?")
  beep = int(input())
  print("What is thwe weight of Bop?")
  bop = int(input())
  print("Please enter either sum or average")
  answer = input()
  if answer == "sum":
    sum_weights(beep,bop)
  
  elif answer == "average":
    calc_avg_weight(beep,bop)
    
  else:
    print("Please enter sum or average")

run()