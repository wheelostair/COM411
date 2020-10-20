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

  return response

def run():
  route = []
  print("Working out escape route...")

  loop = 0

  while loop < 5:
    answer = menu()
    loop = loop +1
    for index in range(answer):
      route.append("{}".format(answer[index]))
  print("Escape route:{}".format(route))

run()
