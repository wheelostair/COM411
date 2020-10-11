print("How many rows should I have?")

rows = int(input())

print("How many columns should I have?")

cols = int(input())

print("Here I go:")

for row in range(0, rows, 1):
  for cols in range(0, cols, 1):
    print(":)" ,end="")
  print()
print("Done!")