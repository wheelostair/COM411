def observed():
  observations = []

  for count in range (5):
    print("Please Enter an observation")
    observations.append(input())
  return observations

def remove_observation(observations):

  is_running = True
  while(is_running):
    print("Do you wish to remove an observation (yes/no)?")
    answer = input()
    if (answer == "yes"):
      print ("What observation do you wish to remove?")
      observation_remove = input()
      observations.remove(observation_remove)
    else:
      is_running = False


def run():
  observations = observed()
  remove_observation(observations)
  observed_set = set()

  for observation in observations:
    occurrences = observations.count(observation)
    observed_set.add((observation,occurrences))
  
  for key, value in sorted(observed_set):
    print("{} observed {} times".format(key,value))
  
run()