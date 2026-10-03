# ct=3
# while ct>=0:
#     std=input("Enter your Name: ")
#     ct-=1


# r " " before a file path tells Python to read the path exactly as written, so \ is treated as a normal character.
file=open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\stud_details.txt","r")
print(file.read())
# When you open a file using open(), you should close it using file.close() after you're finished using it.
# file.close()


# to work  with the file which is already opened.
# when the file does not exist it shows an error . Pointer starts at beginning
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\stud_details.txt","r")as file:
    content=file.read()
    print(content)


#  with open -> it will open the file and close it automatically 



# how many char's to read
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\stud_details.txt","r")as file:
    # Reads only the first 7 characters from the entire file and stores them in content.
    content=file.read(7)
    print(content)


# Append a content in existing file
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\stud_details.txt","a")as file:
        content="Kayalvizhi"
# write - write a string to a file . It does not automatically add new line..so type newline="" after "a".
        file.write(content)
        print("Done")


# write - if the file does not exist it creates new one and write or completely replace with the new content if exists
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\stud_details.txt","w")as file:
     file.write("Shiva")

# r+ = Read + Write, without deleting or replace existing content.
# it based on the word length
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\stud_details.txt","r+")as file:
    file.write("Sakthi")
    content=file.read()
    print(content)

# w+ = Write + Read, but clear the old content first.    
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\stud_details.txt","w+")as file:
    file.write("Sendhazhini")
    # file.seek(0) → moves back to the beginning.
    file.seek(0)
    print(file.read())


# a+ => performs both Append and  Read, keep old content.
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\stud_details.txt","a+")as file:
    file.write("\nRiyazhini")
    # file.seek(0) → moves back to the beginning.
    file.seek(0)
    print(file.read())

# readlines() reads all lines of a file and returns them as a list.
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\stud_details.txt","r")as file:
    content=file.readlines()
    print(content)


# writelines() = write multiple lines from a list.
# ⚠️ It doesn't automatically add \n, so add \n yourself if you want each item on a new line.   

students=["Kanish\n","Tanish\n","Manish\n"]
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\stud_details.txt","w")as file:
     file.writelines(students)

# readline() → Reads one line at a time from the file and returns that line as a string.
# readlines() → Reads all remaining lines at once and returns them as a list of strings.



# readline() → Reads one line at a time from the file and returns that line as a string.
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\stud_details.txt","r")as file:
    print(file.readline())
    print(file.readline())

# ({print(file.readline())   # Kanish
# print(file.readline())   # Tanish
# print(file.tell())       # 16})

# ([ Calculation:
# Kanish = 6 characters
# New line (\r\n) = 2
# First line = 6 + 2 = 8
# Tanish = 6 characters
# New line = 2
# Second line = 6 + 2 = 8
# 8 + 8 = 16
# tell() = 16 → cursor is at position 16 after reading the first 2 lines.])
    
    print(file.tell())
