#imports module os
import os

#define function to retrieve file path
def cwd():
  path = os.getcwd()

  #display current working folder
  print("The current working folder is {}".format(path))
  
  print("The folder contains the following:")
  #display files in folder
  for file in os.listdir(path):
    print(file)

#define function to run previos function
def run():
  print("Processing...")
  cwd()
  
run()