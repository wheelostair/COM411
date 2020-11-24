import matplotlib.pyplot as plt

def player():
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 945fc7b4426834a26fa0d7eff1b03b787c58fbc7
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

<<<<<<< HEAD
=======
=======
  player_name = []
  goals_scored = []
  for count in range (5):
    print("Please enter a player name.")
    name = input()
    player_name.append(name)
    print("How many goals has the player scored?")
    goals = input()
    goals_scored.append(goals)

  return player_name
  return goals_scored

def pie():
  data = player()
  other = player()
  labels = (data)
  goal = (other)
  plt.pie(goal,labels=labels)
  plt.show()
  

pie()
>>>>>>> a3c4acb708fbdc05fa0062c0a673d990eecf96c7
>>>>>>> 945fc7b4426834a26fa0d7eff1b03b787c58fbc7
