def short_pattern():
  pattern = {"sequence":"101","occurences":5}
  return pattern

def medium_pattern():
  pattern = {"sequence":"111000", "occurrences": 25}
  return pattern

def long_pattern():
  pattern = {"sequence":"1100110011001100","occurrences":50}
  return pattern

def run():
  print("Analysing patterns...")

  patterns = {"short sequence":short_pattern(), "Medium sequence":medium_pattern(), "Long sequence":long_pattern()}

  print(patterns)

run()