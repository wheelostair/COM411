def movements():
  path = ["Move Forward",10,"Move Backward", 5,"Move Left",3,"Move Right",1]
  return path

def run():
  print("Moving...")
  movements()

  move = movements()

  print("{} for {} steps".format(move[0],move[1]))
  print("{} for {} steps".format(move[2],move[3]))
  print("{} for {} steps".format(move[4],move[5]))
  print("{} for {} steps".format(move[6],move[7]))


  for index in range(0,len(move),2):
    print("{} for {} steps".format(move[index],move[index+1]))

run()