import matplotlib.pyplot as plt

def player():
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