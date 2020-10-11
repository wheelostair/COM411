print("What strange markings do you see?")

marking = input()

print("Identifying...")

for position in range (0, len(marking),1):
  print("Index",position,":" ,marking[position])

print("Done!")