import matplotlib.pyplot as plt

def player():
  print("Please enter a player name.")
  name = input()
  
  print("How many goals has the player scored?")
  goals = int(input())
  
  return (name,goals)




def amount():
  
  first_name=[]
  scored=[]
  print("How many players do you want to track?")
  answer = int(input())
  for a in range(answer):
    data = player()
    first_name.append (data[0])
    scored.append (data[1])
  
  labels = [first_name]
  goals = [scored]
  print (labels)
  print (goals)
   

amount()

