print("What type of cover (soft or hard) does the book have?")
cover = input()

if (cover == "soft"):
  print("Is the book perfect-bound?")
  answer = input()

  if (answer == "yes"):
    print ("Soft cover, perfect bound books are very popular!")
  else:
    print ("This is a soft cover book.")

elif(cover == "hard"):
  print ("The book is hard back.")

else:
  print ("the book is",cover,"back")