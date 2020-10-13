def escape_by(plan):
  if plan == "jumping over":
    print("We cannot escape that way! the boulder is too big!")
  elif plan == "running around":
    print("We cannot escape that way! The boulder is moving too fast!")
  elif plan == "going deeper":
    print("That just might work! Let's go deeper!")
  else:
    print("We cannot escape that way! The boulder is in the way!")

escape_by("breaking the boulder")
