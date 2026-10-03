# value error

# i/p  = 45 , o/p =45
# i/p = Fourty Five ,  o/p =Value error
# because in 2nd i/p value is a string but actual code is ask for int value

try:
   age=int(input("Enter age: "))
   print(age)

except ValueError:
   print("Please enter age in numbers")



# file not found error
try:
   with open(r"std_marks.txt","r")as file:
      file.read()

except FileNotFoundError:
   print("File does not exist please create a file")



# permission error

try:

# the try block wil execute when the file path is a file inside a folder.
    with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\File_handling\prctcepanda.ipynb")as file:

# the except block wil print when the file path is folder.Because it doesn't open directly a folder so it throws sum error
    # with open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Python\Error_handling")as file:

      data = file.read()
    #   file.write()
      # (or)
    print(data)

except PermissionError:
 print("You can only read this file  and it can't be written")



# to open a text file in readmode

file = open(r"C:\Users\ELCOT\Desktop\JananiMurugan\Excel\Projects\FreshMart\FM_README_md\README.md", "r")
print(file.read())
file.close()


# here if the value is correct else block will work otherwise exceptional block works

try:
    a=int(input("Enter a number:"))
except:
    print("Enter valid number")
else:
    print("valid number",a)

# types of errors in python
# 1. FileNotFoundError
# 2. PermissionError
# 3. FileExistsError
# 4. OSError
# 5. IsADirectoryError


# when we don't know what is the exact error so can use just except block
try:
    age=int(input("Enter your  age: "))
    print(age)

except:
    print("Please enter age in numbers")


# finally block in Python :-
# The finally block always executes, whether an error occurs or not.
# It is commonly used to close a file or clean up resources.

try:
    a = int(input("Enter a number:"))
except ValueError:
    print("Enter a valid number")
else:
    print("Valid number:", a)
finally:
    print("Program completed")


# the follwing code shows which block is completed

block = ""

try:
    a = int(input("Enter a number:"))
    block = "try"

except ValueError:
    print("Enter a valid number")
    block = "except"

else:
    print("Valid number:", a)
    block = "else"

finally:
    print(block, "block completed")
    print("Program completed")



# continously run the code
while True :
    try:
       att=int(input("Enter attendance:"))
       if  not 0<=att<=100:
             raise ValueError("Kindly enter valid attendance between 0 to 100")
       else:    
             print("attendance: ",att)
       break
    except ValueError as error:
         print("Invalid Attendance")