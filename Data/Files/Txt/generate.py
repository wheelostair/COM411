def search(file_name):
  print("Searching...")
  data = {}
  with open(file_name)as file:
    section_name = ""
    split = ""
    for line in file:
      if line.startswith("Section"):
        split = line.split(":")
        section_name = split[1].strip()
      else:
        if (section_name in data):
          values = data[section_name]
          values.append(line.strip())
        else:
          data[section_name] = [line.strip()]
  print("Done!")
  return data

  

def run():
  data = search("Data/Files/Txt/books.txt")

  with open("Data/Files/Txt/generated.csv","w")as file:
    for item in data.items():
      section = item[0]
      books = item[1]
      file.write(section)
      for book in books:
        file.write(", {}".format(book))
      file.write("\n")
  
run()