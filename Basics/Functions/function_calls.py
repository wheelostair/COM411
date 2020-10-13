def box(word):
  print(""" 
  -------------
  |{}|
  -------------
""".format(word))

def lower(word):
  print (word.lower())

def upper(word):
  print (word.upper())

def mirror(word):
  print(word, "|" ,word[::-1])

def repeat(word):
  print("How any times would you like to display the word?")
  times = int(input())
  count = 0
  while count < times:
    print (word.upper())
    count += 1
    print (word.lower())
    count += 1

def run():
  print("Please enter a word")

  word = input()

  print("Please choose a function:\n 1)Display in a box\n 2)Display lower case\n 3)Display Upper Case\n 4)Display Mirrored\n 5)Repeat")

  choice = int(input())

  if choice == 1:
    box(word)

  elif choice == 2:
    lower(word)

  elif choice == 3:
    upper(word)
  
  elif choice == 4:
    mirror(word)

  elif choice == 5:
    repeat(word)

  else:
    print("Please choose a number from 1-5")

run()