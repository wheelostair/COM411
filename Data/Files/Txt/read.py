def search(file_name):
  print("Searching...\n")

  with open(file_name) as file:
    for line in file:
      print("Looked in {}".format(line[:-1]))

    print("\n...Done!")

def run():
  search("Data/Files/Txt/locations.txt")

run()