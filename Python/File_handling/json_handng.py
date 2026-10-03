import json

# | Function  | Input         | Output        |
# | --------- | ------------- | ------------- |
# | `dump()`  | Python object | JSON file     |
# | `dumps()` | Python object | JSON string   |
# | `load()`  | JSON file     | Python object |
# | `loads()` | JSON string   | Python object |


# ([dump() → Takes Python data and writes it into a JSON file.
# dumps() → Takes Python data and converts it into a JSON string.
# load() → Takes data from a JSON file and converts it into Python data.
# loads() → Takes a JSON string and converts it into Python data.

# Easy way to remember:
# dump / load → file 📁
# dumps / loads → string 📝

# The s means string.])


# To load data from a JSON file and display it, use json.load() with print():
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_info.json","r")as j_file:
    student=json.load(j_file)
    print(student["marks"]["Python"]) 

# dump() = writes the Python object to the JSON file; it does not mean “append.” ..it creates and store in a seperate dictionary
# data={"Present":"Yes"}
# with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_info.json","a")as j_file:
#     student=json.dump(data,j_file,indent=2)
#     print(student)


# to  add data using dump() and aslo appends in the existing dictionary
with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_info.json","r")as j_file:
    student=json.load(j_file)

student["Present"]="Yes"

with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_info.json","w")as j_file:
    json.dump(student,j_file,indent=2)
    # print(student)



# dumps() is used to convert Python data into a JSON string.

with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\std_info.json","r")as j_file:
    l=json.load(j_file)
result=json.dumps(l)
print(result)


# json.loads() is used to convert a JSON string into a Python object.  
data='{"name":"Aadhav","marks":"85"}'
student=json.loads(data)
print(student)
print(type(student))