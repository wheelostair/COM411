#Ask users name
print("What is your name human?")
name = input()
#Ask users age
print("How old are you (in years)?")
age = int(input())
#Ask users height
print("How tall are you (in meters)?")
height = float(input())
#Ask Users weight
print("how much do you weigh (in kilograms)?")
weight = float(input())
#Calculate BMI
print(name, "you are" ,age,"years old and your BMI is" ,weight/(height**2))
