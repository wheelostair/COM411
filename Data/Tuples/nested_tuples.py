def steps():
  likelihoods = []
  likelihoods.append(("Step 1", 50))
  likelihoods.append(("Step 2", 38))
  likelihoods.append(("Step 3", 27))
  likelihoods.append(("Step 4", 99))
  likelihoods.append(("Step 5", 4))
  return likelihoods

def run():
  probs = steps()
  good_steps = []
  bad_steps = []

  for likelihood in probs:
    if (likelihood[1]>= 50):
      bad_steps.append(probs)
    else:
      good_steps.append(probs)


  print("Good Steps: {}, Bad Steps {}".format(len(good_steps), len(bad_steps)))

run()