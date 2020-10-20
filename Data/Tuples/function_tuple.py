def likelihood():
  likelihoods = (50,38,27,99,4)
  return min(likelihoods), max(likelihoods)

def run():
  likelihood()

  local = likelihood()
  print("Minimum likelihood of falling {}%".format(local[0]))
  print("Maximum likelihood of falling {}%".format(local[1]))

run()