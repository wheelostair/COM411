def cross_bridge(steps):
  num = 0
  
  while steps > num:
    print ("Crossed step.")
    num +=1
  if steps >5:
    print ("The bridge is collapsing!")
  else:
    print ("We must keep going!")


  
cross_bridge(6)