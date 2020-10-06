print("How many Bars should be charged?")

bars = int(input())

charged = 0
while (charged < bars):
  charged +=1
  print ("Charging:", "█" *charged)

print ("The Battery is fully charged!")