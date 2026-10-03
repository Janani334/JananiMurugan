# _attendance(if we use _befor the name for protect)
# encapsulation not only give limit. it also protects
# within limits -> setter
# to protect -> getter

class student:
        def __init__(self,name,attendance):
        # protect attendance within the limit of 0 - 100
        def att_set(self,attendance):
             self._attendance=attendance
        # get it when needed to display (getter)
        def attendance(self):
              self._attendance=attendance
    def display(self):
            return f"student name:{self.name} \n attendance:{self.attendance}% "
std1=student("Varunya",90)
print(std1.attendance)