# **************************************************************
#    DON'T DISPLAY MARKS . DISPLAY ONLE CGPA VALUE IN CONSOLE
# **************************************************************


# _attendance(if we use _befor the name for protect)
# encapsulation not only give limit. it also protects
# within limits -> setter
# to protect -> getter

class student:
    university="Nova University"
# self is a current object (instead of giving std1.name,std.name we give self)
    def __init__(self,name,id,dept,marks,att):
              self.name=name
              self.id=id
              self.dept=dept
              self._marks=marks
              self.set_marks()

              # to protect 
              self.att=att 
              if 0 <= att <=100:
                self._att=att
              else:
                raise ValueError("Please enter valid number")
    def display(self):
        return f"Name:{self.name} \n ID:{self.id} \n Department:{self.dept} \n Attendance:{self._att} \n CGPA:{self.CGPA()} "

    def average(self):
        return f"Average:{sum(self._marks)//len(self._marks)}"

# Encapsulation → protects and controls access to data
    #  Getter = a method used to get/read the value of a private or protected attribute.   
# getter will display the att when it is given
# Getter → gets/reads the protected data
    def get_attendance(self):
            return self._att     


# Setter = a method used to set/change the value of a private or protected attribute.  
# # Setter → changes/validates the protected data       
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
                if not 0 <= i <= 100:
                      raise ValueError("Enter marks b/w 0 to 100")


std1=student("Arun","CS101","CSE",[78,50,35],89)
std2=student("Varun","CS102","CSE",[48,60,95],97)                

print(std1.display()) 

print(std2.display())


