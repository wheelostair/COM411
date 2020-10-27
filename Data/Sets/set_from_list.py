def observed():
  observations = []

  for count in range (7):
    print("Please Enter an observation")
    observations.append(input())
  return observations

def run():
  print ("Counting observations...")
  observations = observed()
  observed_set = set()

  for observation in observations:
    observed_set.add((observation,observations.count(observation)))
  
  print(observed_set)
  
run()
