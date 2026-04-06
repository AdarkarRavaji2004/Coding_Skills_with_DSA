# class Student:
#     roll_no = 101   #data member

#     def studentData(self):  #method/member function
#         print("Student Information")

# obj = Student()
# print(obj.roll_no)
# obj.studentData()

#-------------------------------------------------------------------------------------

# class Demo:
#     def __init__(self):
#         print("I am Constructor")

#     def msg(self):
#         print("Hello class")

# obj1 = Demo()
# # print(obj1)
# obj2 = Demo()
# obj1.msg()

#-----------------------------------------------------------------------------
# class Hod:
#     def __init__(self): #constructor
#         self.name = "Prashant Jha"
#         self.age =  53
#         self.empid = 1001
#     def info(self):
#         print("My name is ",self.name)
#         print("My Age is :",self.age)
#         print("My emp id :",self.empid)
# obj = Hod()
# obj.info()

#----------------------------------------------------------------------------------
# class Hod:
#     def __init__(self,name,age,rollno): #constructor
#         self.name = name
#         self.age =  age
#         self.rollno = rollno

#     def show(self):
#         print("My name is ",self.name)
#         print("My Age is :",self.age)
#         print("My Roll No is :",self.rollno)
# obj = Hod('Argun',45,101)
# obj.show()

#--------------------------------------------------------------
# class New:
#     def __init__(self):
#         self.a =10

# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# print()
# obj1.a = 20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#------------------------------------------------------------------------

#declaring instance variable outside a class by using object

# class Student:
#     def __init__(self):
#         self.s_name = "prashant"
#         self.s_rollNo = 101     #declaring a instance var inside a constructor

#     def getdata(self):
#         self.s_mb = 1223344556  #declaring a instance var inside a instance method

# obj = Student()
# obj.getdata()
# print(obj.s_name)
# print(obj.s_rollNo)
# print(obj.s_mb)
# del obj.s_mb            #deleting instance variable using obj
# obj.s_branch = "CS"     #adding instance variable by using obj
# print(obj.__dict__)

#-------------------------------------------------------------------
# class New:
#     a = 10  #static var
#     def __init__(self):
#         self.name = "prashant"  #instance var

# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# New.a = 50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#--------------------------------------------------------------------------
# import sys

# class CRUD:
#     def _init_(self):
#         print("Student Management System")
#         self.studentID=[]
#         self.studentName=[]
#         self.studentRollNo=[]
#         self.studentCity=[]

#     def addStudent(self):
#         self.studentID.append(input("Enter student ID: "))
#         self.studentName.append(input("Enter student name: "))
#         self.studentRollNo.append(input("Enter student roll no: "))
#         self.studentCity.append(input("Enter student city: "))

#     def ShowStudent(self):
#         if not self.studentID:
#             print("No students to display")
#             return
        
#         # Print table header
#         print("\n" + "="*80)
#         print(f"{'ID':<10} {'Name':<20} {'Roll No':<10} {'City':<20}")
#         print("="*80)
        
#         # Print student data in table format
#         for i in range(len(self.studentID)):
#             print(f"{self.studentID[i]:<10} {self.studentName[i]:<20} {self.studentRollNo[i]:<10}")
#         print("="*80)
#         print()

#     def updateStudent(self):
#         id=input("Enter student ID to update: ")
#         if id in self.studentID:
#             index=self.studentID.index(id)
#             self.studentName[index]=input("Enter new student name: ")
#             self.studentRollNo[index]=int(input("Enter new student roll no"))
#             self.studentCity[index]=input("Enter new student city: ")
#             print("Student updated successfully")
#         else:
#             print("Student ID not found")

#     def deleteStudent(self):
#         id=input("Enter student ID to delete: ")
#         if id in self.studentID:
#             index=self.studentID.index(id)
#             del self.studentID[index]
#             del self.studentName[index]
#             del self.studentRollNo[index]
#             del self.studentCity[index]
#             print("Student deleted successfully")
#         else:
#             print("Student ID not found")

# obj=CRUD()
# while True:
#     print("1. Add Student")
#     print("2. Show Student")
#     print("3. Update Student")
#     print("4. Delete Student")
#     print("5. Exit")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         obj.addStudent()
#     elif choice==2:
#         obj.ShowStudent()
#     elif choice==3:
#         obj.updateStudent()
#     elif choice==4:
#         obj.deleteStudent()
#     elif choice==5:
#         sys.exit()
#     else:
#         print("Invalid choice")


#-------------------------------------------------------------------------------------

# import sys
# class CRUD:
#     def __init__(self):
#         print("Student Management System")
#         self.studentId=[]
#         self.studentName=[]
#         self.studentRollNo=[]
#         self.studentCity=[]
#     def addStudent(self):
#         self.studentId.append(input("Enter student Id :"))
#         self.studentName.append(input("Enter student Name :"))
#         self.studentRollNo.append(input("Enter student Roll No :"))
#         self.studentCity.append(input("Enter student City :"))
#     def ShowStudent(self):
#         print("Student ID: \t\t StudentName \t\t StudentRollno \t\t City")

        
#         for i in range(len(self.studentId)):
            
            
        
#             print("----------------------------------------------------------------------------------")
#             print(self.studentId[i],"\t\t\t",self.studentName[i],"\t\t\t",self.studentRollNo[i],"\t\t\t",self.studentCity[i])
#             print("----------------------------------------------------------------------------------")
#     def updateStudent(self):
#         id = int(input("Enter student ID to update:"))
#         if id in self.studentId:
#             index = self.studentId.index(id)
#             print("1. Update Name")
#             print("2. Update Roll No")
#             print("3. Update City")
#             choice = int(input("Enter your choice: "))
#             if choice == 1:
#                 self.studentName[index] = input("Enter new name: ")
#             elif choice == 2:
#                 self.studentRollNo[index] = int(input("Enter new roll number: "))
#             elif choice == 3:
#                 self.studentCity[index] = input("Enter new city: ")
#             else:
#                 print("Invalid choice.")
    
#         print("Student updated successfully.")

#     def deleteStudent(self):
#         id=input("Enter student ID to delete: ")
#         if id in self.studentId:
#             index=self.studentId.index(id)
#             del self.studentId[index]
#             del self.studentName[index]
#             del self.studentRollNo[index]
#             del self.studentCity[index]
#             print("Student deleted successfully")
#         else:
#             print("Student ID not found")
# obj=CRUD()
# while True:
#     print("1. Add Student")
#     print("2. Show Student")
#     print("3. Update Student")
#     print("4. Delete Student")
#     print("5. Exit")
#     choice=int(input("Enter your choice: "))
    
#     if choice==1:
#         obj.addStudent()
#     elif choice==2:
#         obj.ShowStudent()
#     elif choice==3:
#         obj.updateStudent()
#     elif choice==4:
#         obj.deleteStudent()
#     elif choice==5:
#         sys.exit()
#     else:
#         print("Invalid choice")


#--------------------------------------------------------------------------
# instance Method

# class Student:
#     def __init__(self,name,rollno,mob):
#         self.name= name
#         self.rollno = rollno
#         self.mob = mob

#     def display(self):
#         print(self.name," ",self.rollno," ",self.mob)

# stud = Student("Prashant",1001,9876452365)
# stud.display()
    
#-----------------------------------------------------------------------------------
#Static Method

# class Student:
#     #by using class name we can access static method
#     @staticmethod   #decorated
#     def get_personal_detail(firstname,lastname):
#         print("your oersonal details :",firstname,lastname)

#     @staticmethod
#     def contact_detail(mobile_no,rollno):
#         print("your contact detail :",mobile_no,rollno)
        
# Student.get_personal_detail("prashant","jha")
# Student.contact_detail(8976542386,1001)

#=============================================================================================

#Inheritance =
# Extending the properties from one class to another class is called inheritance
# Base class : A class which is inherited by another class is called parent class
# Derived class : A class which inherits the properties of another class is called child class
#Types of Inheritance :
# 1. Single Inheritance : A class inherits the properties of another class
# 2. Multilevel Inheritance : A class inherits the properties of another class which is also inherited by another class
# 3. Multiple Inheritance : A class inherits the properties of more than one class
# 4. Hierarchical Inheritance : More than one class inherits the properties of a single class
# 5. Hybrid Inheritance : A combination of two or more types of inheritance

#=============================================================================================
#Single Inheritance
# class College:      #parent class
#     def college_name(self):    #member function of college
#         print("Mordern College")

# class Student(College):         #child class
#     def student_info(self):     #member function 
#         print("Name : Prashant Jha")
#         print("Branch : Computer Science")
    
# obj = Student()     #object create child class
# obj.college_name()
# obj.student_info()

#--------------------------------------------------------------------------------------------

#Multilevel Inheritance
# class College:                  #first class
#     def college_name(self):    
#         print("Mordern College")

# class Student(College):         #second class
#     def student_info(self):      
#         print("Name : Prashant Jha")
#         print("Branch : Computer Science")

# class Exam(Student):
#     def subject(self):
#         print("Subject1 : Design Engineering")
#         print("Subject2 : Mathematics")
#         print("Subject3 : C-Language")
# obj = Exam()    
# obj.college_name()
# obj.student_info()
# obj.subject()


#--------------------------------------------------------------------------------------------

# class SubjMarks:
#     math = int(input("Enter paper marks of math :"))
#     eng = int(input("Enter paper marks of english :"))
#     sci = int(input("Enter paper marks of science :"))
#     c = int(input("Enter paper marks of c language :"))

# class Practmarks:
#     cpract = int(input("Enter practical marks of c language :"))

# class Result(SubjMarks,Practmarks):
#     def total(self):
#         if self.math >= 40 and self.eng >= 40 and self.sci >= 40 and self.c >= 40 and self.cpract >= 20:
#             print("pass")
#         else:
#             print("fail")
# obj = Result()
# obj.total()

#==============================================================================================

#Polymorphism = The ability of an object to take many forms is called polymorphism
#Types of Polymorphism :
# 1. Compile time Polymorphism : The ability of a function to perform different tasks based on the number of arguments passed is called compile time polymorphism
# 2. Run time Polymorphism : The ability of a function to perform different tasks based on the type of arguments passed is called run time polymorphism

# class Principal:
#     def role(self):
#         print("i am managing all activities of college")

# class Dean:
#     def role(self):
#         print("Dean= I am decision taking person")

# class Hod:
#     def role(self):
#         print("Hod= I have responcibility of Teachers and Students")

# class Faculty:
#     def role(self):
#         print("Faculty= I have to complete syllabus successfully")

# def fun(obj):
#     obj.role()
# campus = [Principal(),Dean(),Hod(),Faculty()]
# for obj in campus:
#     fun(obj)


#Python does not support method overloading but we can achieve it by using default arguments
# class Arithmetic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)    

# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)


#=--------------------------------------------------------------------------------------------

# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None:
#             print(a+b)
#         elif a!=None and b!=None and c!=None:
#             print(a+b+c)
#         else:
#             print("Enter at least two arguments")
# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)

#--------------------------------------------------------------------------------------------

# class Arithmetic:
#     def __init__(self):
#         print("Ther is no argument")
#     def __init__(self, a):
#         print("passing one argument :")
#     def __init__(self, a, b):
#         print("passing two argument :")

# obj = Arithmetic()
# obj = Arithmetic(10)
# obj = Arithmetic(2,2)

#--------------------------------------------------------------------------------------------
#Method Overriding = The ability of a child class to provide a specific implementation of a method that is already provided by its parent class is called method overriding
#Overrrinding python supports

# class Rbi:
#     def home_loan(self):
#         print("Home loan = 7.5")
#     def car_loan(self):
#         print("Car loan 8 %")

# class Sbi(Rbi):
#     def home_loan(self):
#         print("Sbi provides home loan = 6.5")
#         super().home_loan()   #super() is used to call the parent class method

# obj = Sbi()
# obj.home_loan()     #child class method overrides the parent class method
# obj.car_loan()      #parent class method is called because child class does not have this

#------------------------------------------------------------------------------------------

#Constructor Overriding = The ability of a child class to provide a specific implementation of a constructor that is already provided by its parent class is called constructor overriding

class Father:
    def __init__(self):
        print("Father := i am allready at breafast table")

class Child(Father):
    def __init__(self):
        print("Child := i will be late for breakfast")
        super().__init__()   #super() is used to call the parent class constructor

obj = Child()     #child class constructor