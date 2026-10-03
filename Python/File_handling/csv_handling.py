import csv  

with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_data.csv","r")as file:

# here reader reacts as a cursor
    reader=csv.reader(file)

# To iterate through data and to print it and it will print exactly how it is present in the csv file
    for line in file:
        print(line)

# it prints addr        
    print(reader)

# dict reader will help to treat as dictionary and to  display the data
    reader=csv.DictReader(file)
    for i in reader:
        print(i["Name"],i["Dept"])
        # (or)
        print(i["Dept"])



with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_data.csv","w")as file:
    # to write a content in csv file
       writer=csv.writer(file)
       writer.writerow(["Yaazhini","Animation"])


with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_data.csv","a",newline="")as file:
    # To add content in csv file
       writer=csv.writer(file)
       writer.writerow(["Yaazhini","Animation"])
      

# to write multiple rows
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_data.csv","w")as file:
           writer=csv.writer(file)
           writer.writerow([["Yaazhini","Animation"],["Iniyazh","BE"]])


# Write row using  DictWriter
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_data.csv","w",newline="")as file:
      fieldname=["Name","Dept"]
      writer=csv.DictWriter(file,fieldnames=fieldname)
      writer.writeheader()
      writer.writerow({"Name":"a","Dept":"CSE"})


# write rows using DictWriter
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_data.csv","w",newline="")as file:
      fieldname=["Name","Dept"]
      writer=csv.DictWriter(file,fieldnames=fieldname)
      writer.writeheader()
      writer.writerows([
            {"Name":"Yaazhini","Dept":"Animation"},
            {"Name":"Iniyazh","Dept":"BE"},
            {"Name":"Anu","Dept":"ME"},
            {"Name":"Raghavi","Dept":"CSE"}
      ])


    #   or another method

stds = [
    {"Name":"Yaazhini","Dept":"Animation"},
    {"Name":"Iniyazh","Dept":"BE"},
    {"Name":"Anu","Dept":"ME"},
    {"Name":"Raghavi","Dept":"CSE"}
]
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_data.csv","w",newline="")as file:
      writer=csv.DictWriter(
            file,
            fieldnames=["Name","Dept"]
      )
      writer.writeheader()
      for student in stds:
            writer.writerow(student)

