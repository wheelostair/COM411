print("Which room should I look in?")
room = input()

if (room == "bedroom"):
  print ("Where in the bedroom should i look?")
  bedroom = input()
  if (bedroom == "under the bed"):
    print ("Found some shoes, but no battery")
  else:
    print ("Found some mess, but no battery.")

elif (room == "bathroom"):
  print ("Where in the bathroom should i look?")
  bathroom = input()
  if (bathroom == "in the bathtub"):
    print ("Found a rubber duck, but no battery")
  else:
    print ("Found a wet surface, but no battery.")

elif (room == "lab"):
  print ("Where in the lab should i look?")
  lab = input()
  if (lab == "on the table"):
    print ("Yes!! I found my Battery!")
  else:
    print ("Found some tools, but no battery.")

else:
  print("I do not know where that is, but I will keep looking.")