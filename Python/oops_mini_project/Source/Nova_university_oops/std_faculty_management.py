# ***************************************************************************************************
#                         UNIVERSITY MANAGEMENT (STAFF AND FACULTY DETAILS)
# ***************************************************************************************************



# ****************************************************************************************************
#                                        PERSON INFORMATION
# ****************************************************************************************************

# to create a class named as person
class person:
    def __init__(self,name,email,mob_no):
        self.name=name
        self.email=email
        self.mob_no=mob_no
    def display_role(self):
        return "University Person"
    

# ****************************************************************************************************
#                                        STUDENT INFORMATION
# ****************************************************************************************************

# Create student class
class student(person):
    def __init__(self,std_id,name,email,mob_no,dept,att,python_marks,sql_marks,excel_marks):
        super().__init__(name, email,mob_no)
        self.std_id=std_id
        self.dept=dept
        self.att=self.validate_att(att)
        self.python_marks=self.validate_marks(python_marks)
        self.sql_marks=self.validate_marks(sql_marks)
        self.excel_marks=self.validate_marks(excel_marks)
    def display_role(self):
        return "Student"


# ****************************************************************************************************
#                                        ACADEMIC CALCULATIONS
# ****************************************************************************************************

# calculations(total,avg) , result status and grade

# Total
    def total(self):
        return self.python_marks + self.sql_marks + self.excel_marks

# Average
    def average(self):
        return self.total() / 3

# Result status
    def status(self):
        if self.average() >= 50:
            return "Pass"
        else:
            return "Fail"

# Grade

# 90–100 → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# 50–59 → E
# Below 50 → F

    def grade(self):
        if self.average() >= 90:
            return "Grade A"
        elif self.average() >= 80:
            return "Grade B" 
        elif self.average() >= 70:
            return "Grade C" 
        elif self.average() >= 60:
            return "Grade D"
        elif self.average() >= 50:
            return "Grade E"
        else:
            return "Grade F"  


# Attendance Eligibility
    def att_eligibilty(self):
        if self.att >= 75:
            return "Eligible for Examination"
        else:
            return "Not Eligible"

    def validate_att(self,value):
        if 0 <= value <= 100:
            return value
        else:
            raise ValueError("Please Enter a valid Att between 0 to 100")

# for checking whether it is a validate mark or not
    def validate_marks(self,value):
        if 0 <= value <= 100:
            return value
        else:
            raise ValueError("Please Enter valid Marks between 0 to 100") 


# ****************************************************************************************************
#                                        FACULTY INFORMATION
# ****************************************************************************************************

# Create class for Faculty
class faculty(person):
    def __init__(self,faculty_id,name,email,mob_no,dept,subject,experience):
        super().__init__(name,email,mob_no)
        self.faculty_id=faculty_id
        self.dept=dept
        self.subject=subject
        self.experience=experience
    def display_role(self):
        return "Faculty"        



# *****************************************************************************************************
#                                   EXPECTED APPLICATION FLOW
# *****************************************************************************************************

students=[]
faculties=[]


def  show_menu():
        print("1. Add Students")
        print("2. View Students")
        print("3. Check Attendance Eligibility")
        print("4. View Academic Result")
        print("5. Add Faculty")
        print("6. View Faculty")
        print("7. Exit")

        return input("Enter your choice: ")
# choice = show_menu()

# *****************************************************************************************************
#                                            ADD STUDENTS
# *****************************************************************************************************

def add_student():
        try:
            std_id=input("Enter Student ID: ")
            name=input("Enter Name: ")
            email=input("Enter Email: ")
            mob_no=int(input("Enter Mobile_number: "))
            dept=input("Enter Department: ")
            att=float(input("Enter Attendance: "))
            python_marks=float(input("Enter python mark: "))
            sql_marks=float(input("Enter sql mark: "))
            excel_marks=float(input("Enter excel mark: "))
            new_student = student( 
                std_id, 
                name, 
                email, 
                mob_no, 
                dept, 
                att, 
                python_marks, 
                sql_marks, 
                excel_marks ) 
            
            students.append(new_student) 
            print("\nStudent added successfully.") 
        except ValueError as error:
                print("\nInvalid input:", error)



# ***************************************************************************************************** 
#                                            VIEW STUDENTS
# ***************************************************************************************************** 

def view_students():
    if not students:
        print("\n No students available.")
        return

    print("\n*************** STUDENT DETAILS ***************")
    for std in students:
        print("\nStudent_ID: ",std.std_id)
        print("Name :", std.name) 
        print("Email :", std.email) 
        print("Mobile No :", std.mob_no) 
        print("Department :", std.dept)
        print("Attendance :", std.att) 
        print("Role :", std.display_role())



# ***************************************************************************************************** 
#                                        CHECK  ATTENDANCE ELGIBILITY
# ***************************************************************************************************** 

def check_attendance(): 
        if not students: 
            print("\nNo students available.") 
            return 
        std_id = input("Enter Student ID: ") 
        for std in students: 
            if std.std_id == std_id: 
                print("\nAttendance :", std.att) 
                print("Status :", std.att_eligibilty()) 
                return
        print("\nStudent not found.")




# ***************************************************************************************************** 
#                                          VIEW ACADEMIC RESULT
# ***************************************************************************************************** 

def view_academic_result(): 
        if not students: 
            print("\nNo students available.") 
            return 
        std_id = input("Enter Student ID: ") 
        for std in students: 
            if std.std_id == std_id: 
                print("\n*************** ACADEMIC RESULT ***************") 
                print("Student ID :", std.std_id) 
                print("Name :", std.name) 
                print("Python Marks :", std.python_marks) 
                print("SQL Marks :", std.sql_marks) 
                print("Excel Marks :", std.excel_marks) 
                print("Total Marks :", std.total()) 
                print("Average Marks :", std.average()) 
                print("Result :", std.status()) 
                print("Grade :", std.grade()) 
                return 
        print("\nStudent not found.")



# ***************************************************************************************************** 
#                                               ADD FACULTIES 
# ***************************************************************************************************** 

def add_faculty(): 
        faculty_id = input("Enter Faculty ID: ") 
        name = input("Enter Name: ") 
        email = input("Enter Email: ") 
        mob_no = input("Enter Mobile Number: ") 
        dept = input("Enter Department: ") 
        subject = input("Enter Subject: ") 
        experience = input("Enter Experience: ") 
        new_faculty = faculty( faculty_id, name, email, mob_no, dept, subject, experience ) 
        faculties.append(new_faculty) 
        print("\nFaculty added successfully.")




# ***************************************************************************************************** 
#                                               VIEW FACULTY
# ***************************************************************************************************** 

def view_faculty(): 
    if not faculties: 
        print("\nNo faculty available.") 
        return 
    print("\n*************** FACULTY DETAILS ***************") 
    for fac in faculties: 
        print("\nFaculty ID :", fac.faculty_id) 
        print("Name :", fac.name) 
        print("Email :", fac.email) 
        print("Mobile No :", fac.mob_no) 
        print("Department :", fac.dept) 
        print("Subject :", fac.subject) 
        print("Experience :", fac.experience) 
        print("Role :", fac.display_role())  




# ***************************************************************************************************** 
#                                               MAIN PROGRAM
# ***************************************************************************************************** 

print("================================================================================================")
print("                              WELCOME TO NOVA UNIVERSITY                                        ")
print("                              Student Management System                                         ")
print("================================================================================================")

while True: 
    choice = show_menu() 
    if choice == "1": 
        add_student() 
    elif choice == "2": 
        view_students() 
    elif choice == "3": 
        check_attendance() 
    elif choice == "4": 
        view_academic_result() 
    elif choice == "5": 
        add_faculty() 
    elif choice == "6": 
        view_faculty() 
    elif choice == "7": 
        print("\nThank you for using University Management.") 
        break
    else: 
        print("\nInvalid choice. Please enter a number from 1 to 7.")              