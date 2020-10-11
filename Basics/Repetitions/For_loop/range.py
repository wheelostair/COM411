print ("What level of brightness is required?")
level = int(input())

print("Adjusting brightness")
for level in range(2,level +1, 2):
  print("Beep's brightness level:" ,level * "*")
  print("Bop's brightness level:" ,level * "*")

print("Adjustments complete!)")