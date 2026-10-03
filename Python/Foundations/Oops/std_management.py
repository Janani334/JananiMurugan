#  ALT + Z -> is used to wrap  the whole program lines



# to create a template(class)
class student:
# to avoid error in run time / interpreting time when don't know the contents inside the block u can use pass

#    pass
# self is a current object (instead of giving std1.name,std.name we give self)
    def __init__(self,name,id,dept,marks):
              self.university="Nova university"
              self.name=name
              self.id=id
              self.dept=dept
              self.marks=marks
              self.attendance=0
    def display(self):
              return f"university:{self.university} \n Name:{self.name} \n id:{self.id} \n dept:{self.dept} \n marks:{self.marks} \n total:{sum(std1.marks)} \n average:{sum(std1.marks) / len(std1.marks)}  "
              '''
Name
id
dept 
marks
attendance
'''

std1=student("Arun","CS101","CSE",[78,50,35])
std2=student("Varun","CS102","CSE",[48,60,95])


print(std1.name)
print(std1.id)
print(std1.dept)
print(std1.marks)
print(std1.attendance)
print(std2.university)
print(sum(std1.marks))
print(len(std1.marks))
print(sum(std1.marks) / len(std1.marks) )
print(std1.display())
print()
print(std2.display())





# print(type(std1))
# num=9
# print(type(num))

