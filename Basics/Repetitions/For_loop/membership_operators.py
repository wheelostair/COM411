print("What phrase do you see?")

phrase = input()

print("Reversing... \n The phrase is:", end= "")
reverse = ""

for letter in phrase:
  reverse = letter + reverse

print (reverse)