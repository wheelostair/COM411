def search(file_name):
  print("Searching...")
  sections = []
  books = []
  with open(file_name)as file:
    for line in file:
      if line.startswith("Section"):
        split = line.split(":")
        sections.append(split[1][:-1])
      else:
        books.append(line[:-1])
  print("Done!")
  data = (sections,books)
  
  return data



def save(file_name,data):
  print("Saving...")
  
  sections = ""
  books = ""
  
  with open(file_name,"w")as file:
    sections += "Sections: " 
    for section in data[0]:
      sections += section +", "
    books += "\nBooks: "
    for book in data[1]:
      books += book +", "

    file.write(sections[:-2])
    file.write(books[:-2])
    print("Done!")


def run():
  data = search("Data/Files/Txt/books.txt")

  save("Data/Files/Txt/section-books.txt",data)

run()