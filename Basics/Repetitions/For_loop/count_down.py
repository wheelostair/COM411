#Get user input
print("How far are we from the cave?")
steps = int(input())
#Print steps remaining
for count in range(steps):
  print(steps, "steps remaining")
  #minus one step
  steps += - 1

print("We have reached the cave!")