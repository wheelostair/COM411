def likelihood():
  likelihoods = (50,38,27,99,4)
  return min(likelihoods)

def run():
  likelihood()

  local = likelihood()

  print("Minimum likelihood of falling {}%".format(local))

run()