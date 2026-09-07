# Only text will be printed without quotes
print("Hellow World!")

# Text will be printed with the double quotes b'cas it is defined with another single quotes
print ('"Hello world"')

# Text will be printed with the single quotes b'cas it is defined with another double quotes
print("'Hellow World!'")

# Text will be printed with the double quotes b'cas it is defined with another single quotes
print('"my name is janani"')

# returns the reminder 
print(8%2)

# Returns only Quotient (Devision - Integer value returns)
print(8//2)

# Returns float value (Float/ Integer Division)
print(8/2)

# print all in a single line
print(8%7,8/7,8//7)

# print all in new line so we are using \n
print('Name:Janu \nAge:22 \nStream:B.Sc')
Name='Janu'
Age=22
Roll_No='101'

# or use another format
rollNo='101'
print("Name")

# in variables don't mention quotes to display
print(Name)

# Manually entered by the user (So it is user I/P while execution)
# name2=input("enter your name:")
# print("The name of second student is: ",name2)

# another method insteading of using comma (f string)
# (f before the quotation mark tells Python: “I want to insert values inside this text.
# name = "Janani"
# age = 22
# print(f"My name is {name} and I am {age} years old.")
# f"..." → f-string , {name} → gets the value of name, {age} → gets the value of age )

#  print(f"the name of second student is: {name2} and the age of first student is: {Age}")

# print('\"'Hello World'"')?

# To  print 5 students profile ()
print("Std_Name\tAge\tRoll_No\tDegree\tStream\tGender")
print("Elsa\t\t23\tAB101\tM.Sc\tMaths\tF")
print("Aana\t\t26\tAB102\tB.Sc\tIT\tF")
print("Radha\t\t31\tAB103\tB.Tech\tCSE\tF")
print("Krish\t\t21\tAB104\tB.E\tEEE\tF")
print("Kookie\t\t45\tAB105\tB.Sc\tCS\tF")

# To  print 5 students profile (with one print stmt)
print("Std_Name\tAge\tRoll_No\tDegree\tStream\tGender",
"\n Elsa\t\t23\tAB101\tM.Sc\tMaths\tF",
"\n Aana\t\t26\tAB102\tB.Sc\tIT\tF",
"\n Radha\t\t31\tAB103\tB.Tech\tCSE\tF",
"\n Krish\t\t21\tAB104\tB.E\tEEE\tF",
"\n Kookie\t\t45\tAB105\tB.Sc\tCS\tF")

# print student profile by User I/P manner (using loop for many stds)
n= int (input("Enter No.of Students: "))
for i in range(n):
    name=input("Enter your Name: ")
    age=input("Enter your Age: ")
    roll_no=input("Enter your Roll_No: ")
    degree=input("Enter your Degree: ")
    stream=input("Enter your Stream: ")
    gender=input("Enter your Gender: ")
print(f"Student name is:{name}\nage is: {age}\nroll_no is: {roll_no}\ndegree is: {degree}\nstream is: {stream}\ngender is: {gender}")