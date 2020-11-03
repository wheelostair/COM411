def search(file_name):
  print("Searching...")
  data = {}
  with open(file_name)as file:
    for line in file:
      if line.startswith("Section"):
        split = line.split(":")
        data["section"] = (split[1][:-1])
      else:
        data = (line[:-1])
  print("Done!")
  dictonary = {data}
  
  return dictonary

def run():
  data = search("Data/Files/Txt/books.txt")

  print(dictionary)
  
run()