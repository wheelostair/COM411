# Beep is stacking boxes on a shelf depending on their size and weight.
print("What size is the box?")
size = input()
print("How heavy is the box?")
weight = input()

top_shelf = 0
middle_shelf = 0
bottom_shelf = 0

if (size == "big") or (weight =="heavy"):
  bottom_shelf = bottom_shelf +1
  print("This box is Big or Heavy, it should go on the bottom shelf")
  

elif (size == "medium") or (weight == "medium"):
  middle_shelf = middle_shelf +1
  print("This box is medium, it should go on the middle shelf")
  

elif (size == "small") or (weight == "light"):
  top_shelf = top_shelf +1
  print("This box is Light or small, it should go on the top shelf")
  
 
else:
  print("I do not know the size or weight of this box.")


print("The top shelf has",top_shelf,", the middle shelf has",middle_shelf,", the bottom shelf has",bottom_shelf,"boxes")