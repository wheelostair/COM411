print("Please enter a sequence:")

seq = input()

print("Please enter a character for the marker")

marker = input()

mark_pos1 = -1
mark_pos2 = -1

for position in range(0, len(seq),1):
  letter = seq[position]

  if (letter == marker):
    if (mark_pos1 == -1):
      mark_pos1 = position
    else:
      mark_pos2 = position
print("The distance between the markers is:", mark_pos2 - mark_pos1 -1  )