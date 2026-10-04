# ([ the follwoing code means-> importing ABC and abstractmethod from Python's abc module.
# ABC → used to create an Abstract Base Class.
# abstractmethod → used to mark a method that child classes must implement.

# Easy reminder: ABC = abstract class, abstractmethod = compulsory child method. ])

from abc import ABC,abstractmethod
class person(ABC):
    def __init__(self,name,email):
        self.name=name
        self.email=email

# @abstractmethod — definition and use
# Definition: @abstractmethod marks a method in a parent class that must be implemented by the child class.
# Use: It is used to force child classes to provide their own version of that method.        


# abstract method is used to hide the internal operations and also must operations can be done. 
# here abstract method is given when this class is inherited somewhere this method must there or else it will show an error

    @abstractmethod
    def display_role(self):
             return "University Person"

    @abstractmethod
    def display_dashboard(self):
          pass


class student(person):
# super class(parent class), here super consider the previous "class Person as parent node"    
    def __init__(self,name,email,dept):
        super().__init__(name,email)
        self.dept=dept

    # polymorphism
    def display_role(self):
        return "student"

    def display_dashboard(self):
        return "Student Dashboard"

# inherit from student class, and add  a extra instance variable - subjects handled 
# class teacher(student) indicates we inherit the  name,dept,email  from the std    
class teacher(student):
    def __init__(self,name,email,dept,sub_h):
# inherit from student class          
            super().__init__(name,email,dept)
# and add a extra instance variable -subjects handled            
            self.sub_h=sub_h

    # polymorphism
    def display_role(self):
        return "teacher"

    def display_dashboard(self):
            return "Teacher Dashboard"

class hod(person):
    def __init__(self, name, email):
         super().__init__(name, email)

    def display_role(self):
         return "HOD"

    def display_dashboard(self):
         return "HOD Dashboard"

    
# ({[ the following code is only run when your crate a class as class person: only...if you give class person(ABC): ..it shows an error
# as " File "C:\Users\ELCOT\Desktop\JananiMurugan\Python\Foundations\Oops\abstraction.py", line 69, in <module>
#     p1 = person("abc", "abc@gmail.com")
# TypeError: Can't instantiate abstract class person without an implementation for abstract methods 'display_dashboard', 'display_role'"

# class person:
    ...
# you can create the parent class object directly:
# p1 = person("abc", "abc@gmail.com")
# print(p1.display_role())   .....]})


std1=student("Kani","kani@gmail.com","CSE")
print(std1.display_role())

hod1=hod("Moni","moni@gmail.com")
print(hod1.display_dashboard())
     
    