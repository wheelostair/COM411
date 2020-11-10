def directions():
  directions = ["Move Forward","Move Backward","Turn Left","Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  directions()

  local = directions()

  for index in range(len(local)):
    print("{} : {}".format(index,local[index]))

  response = int(input())
  return local[response]

def run():
  route = []
  print("Working out escape route...")

  for count in range(5):
    answer = menu()
    route.append(answer)
  print("Escape route:{}".format(route))

run()
 