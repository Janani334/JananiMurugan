# marks example 1
mark=int(input("Enter your mark:"))
if mark >= 90:
 print("A Grade")
elif mark >= 75 :
 print("B Grade")
elif mark >= 50:
 print("C Grade")
else:
 print("Fail")



# marks example 2
mark=int(input("Enter your mark: "))

if mark>=90:
 print("Excellent")

elif mark >= 75:
 print("Good")

elif mark >= 50:
  print("Pass")

else:
 print("Fail")



# Using nested if statement
mark = int(input("Enter your mark: "))

if mark >= 50:
    print("Pass")

    if mark >= 90:
        print("Excellent")
    elif mark >= 75:
        print("Good")
    else:
        print("Average")

else:
    print("Fail")



# **************
#   10/09/2026
# **************

# Adding numbers from 1 to 11

tot = 0
for  i in range(1,11):
  tot += i;
print(tot)



# for loop using break (note : to change here we can give print stmt before break)
for i in range(1,6):
 if i==3:
    break
print(i)



# while loop
i=1
while i<=5:
    if i==3:
        break
    print(i)
    i+=1



# for loop using continue
for i in range(1,10):
 print(i)
 if i==3:
    continue



# For Loop to Get Student Name and Attendance
for i in range(5):
    name=input("Enter your Name:")
    attendance=int(input("Enter your attendance percentage:"))
  


# Student Attendance Using continue Statement
student_attendance = " "
for i in range(5):
  name=input("Enter your Name:")
  attendance=int(input("Enter your attendance percentage:"))
  if attendance<50:
    continue
  elif attendance==100:
    print(f"{name} - {attendance}%")
    continue
  student_attendance+=(f"{name} - {attendance}%  \n")
print(student_attendance)


  
