#Get user input
print("How far are we from the cave?")
steps = int(input())

for count in range(steps):
  print(steps, "steps remaining")
  steps += - 1

print("We have reached the cave!")