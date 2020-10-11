print("What phrase do you see?")

word = input()

print("Reversing...\n The phrase is:",end="")

for position in range(len(word)-1,-1,-1):
  print (word[position], end="")