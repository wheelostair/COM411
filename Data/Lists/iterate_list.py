def directions():
  directions = ["Move Forward","Move Backward","Turn Left","Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  
  local = directions()

  for index in range(len(local)):
    print("{} : {}".format(index,local[index]))

def run():
  menu()

run()