#  ALT + Z -> is used to wrap  the whole program lines



# to create a template(class)
class student:
    university="Nova University"
# to avoid error in run time / interpreting time when don't know the contents inside the block u can use pass
#    pass

# self is a current object (instead of giving std1.name,std.name we give self)
    def __init__(self,name,id,dept,marks,att):
              self.name=name
              self.id=id
              self.dept=dept
              self._marks=marks
              # to protect
# encapsulation
# Encapsulation = protecting an object's data by keeping it inside the class and controlling how it is accessed or changed.
#  Easy reminder: Encapsulation = data protection.              
# attendance is protected and will not show because it hides so to see use getter and setter
              self.att=att 
              if 0 <= att <=100:
                      self._att=att
              else:
                    raise ValueError("Please enter valid number")
              #  Inside init return or print will not be allowed

             
    def display(self):
              return f"Name:{self.name} \n ID:{self.id} \n Department:{self.dept} \n Attendance:{self._att} \n Marks:{self._marks} \n CGPA:{self.CGPA()} "
    
    
    
    def average(self):
            return f"Average:{sum(self._marks)//len(self._marks)}"


#  Getter = a method used to get/read the value of a private or protected attribute.   
# getter will display the att when it is given
    def get_attendance(self):
            return self._att     


# Setter = a method used to set/change the value of a private or protected attribute.         
    def set_attendance(self,value):
            if 0 <= value <= 100:
                    return value
            else:
                    # raise ValueError("Please enter a valid number")
                    return "Please enter a valid number"


    def CGPA(self):
            avg=sum(self._marks)//len(self._marks)
            self.cgpa=round((avg/10),2)
            return self.cgpa


    def set_marks(self):
            for i in self._marks:
                    if 0 <= self._marks[i] <= 100:
                            self._marks=self._marks
                    else:
                            return "Enter marks b/w 0 to 100"


# To iterate and display all details
stds=[]
num=0
while len(stds)<2:
    m=[]
    n=input("Enter your  Name: ")
    id=input("Enter your ID: ")
    dept=input("Enter your Department: ")
    for i in range(3):
        mrk=int(input(f"Enter your marks for sub{i+1}: "))
        m.append(mrk)
    att=int(input("Enter your attendance: "))
    std=student(n,id,dept,m,att)
    stds.append(std)


for i in range(len(stds)):
        print(stds[i].display())


# Name
# id
# dept 
# marks
# attendance
# '''

# std1=student("Arun","CS101","CSE",[78,50,35])
# std2=student("Varun","CS102","CSE",[48,60,95])


# print(std1.name)
# print(std1.id)
# print(std1.dept)
# print(std1.marks)
# print(std1.attendance)
# print(std2.university)
# print(sum(std1.marks))
# print(len(std1.marks))
# print(sum(std1.marks) / len(std1.marks) )
# print(std1.display())
# print()
# print(std2.display())


# # print(type(std1))
# # num=9
# # print(type(num))

