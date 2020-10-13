print("Program Started!")

print("Please enter an ASCII code:")

code = int(input())

char = chr(code)

if code in range (32,127,1):
  print("The character represented by the ASCII code",code,"is:" ,char)

else:
  print("Please choose a number between 32-126 ")

print("Program ended")