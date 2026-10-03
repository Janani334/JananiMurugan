# # INHERITANCE

class person:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def display_role(self):
         return "University Person"

class student(person):
# super class(parent class), here super consider the previous "class Person as parent node"    
    def __init__(self,name,email,dept):
        super().__init__(name,email)
        self.dept=dept

    def display_role(self):
        return "student"


# inherit from student class, and add  a extra instance variable - subjects handled 
# class teacher(student) indicates we inherit the  name,dept,email  from the std    
class teacher(student):
    def __init__(self,name,email,dept,sub_h):
# inherit from student class          
            super().__init__(name,email,dept)
# and add a extra instance variable -subjects handled            
            self.sub_h=sub_h

    def display_role(self):
        return "teacher"

# # to print university student
# p1=person("abc","abcd@gmail.com")
# print(p1.display_role())

# # to print as student
# std1=student("Kani","kani@gmail.com","CSE")
# print(std1.display_role())

# # to display as teacher
# t1=teacher("xyz","xyz@gmail.com","IT")
# print(t1.display_role())

# # another method to  display it without using variable
# print(person("abc", "abcd@gmail.com").display_role())

# print(student("Kani", "kani@gmail.com", "CSE").display_role())

# print(teacher("xyz", "xyz@gmail.com","IT").display_role())

# Another example
people=[
       student("Jessy","jessy@gmail.com","AI"),
       teacher("Nivi","nivi@gmail.com","IT","python")
]
for person in people:
       print(person.display_role())

