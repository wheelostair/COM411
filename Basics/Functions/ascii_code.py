print("Program Started!")

print("Please enter a letter:")

letter = input()

char = ord(letter)

if (len(letter) == 1):
  print("The ASCII code for" ,letter,"is: " ,char )

else:
  print("Please eneter a single character")

print("Program Ended!")