# def msg():
#     print("Hello World!")

# msg()
# msg()

#---------------------------------------------------------------------------------------------------------
# def arithmatic():
#     a = int(input("Enter the value of A : "))
#     b = int(input("Enter the value of B : "))
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div
# result = arithmatic()
# print("Arithmatic : ",result)

#------------------------------------------------------------------------------------------------------------------
#How many types of argument we can pass in function
# 1.positional argument
# 2.keyword argument
# 3.defaul argument
# 4.variable length argument/variable number of argument

#------------------positional argument-------------------------
# def login(username,password):
#     if username==password:
#         print("Login Successfully")
#     else:
#         print("Invalid Credential")

# username = input("Enter Username : ")
# password = input("Emter Password : ")
# login(username,password)
#----------------keyword argument------------------------------
# def login(username,password):
#     if username==password:
#         print("Login Successfully")
#     else:
#         print("Invalid Credential")

# login(username="admin",password="admin")
#---------------default argument-------------------------------
# def cityName(city="Goa"):
#     print(city)

# cityName("Delhi")
# cityName("Nagpur")
# cityName()
#----------------variable length argument-----------------------
# def nameOfCitys(*city):
#     print("City Name's = ",city)

# nameOfCitys("Goa","Nagpur","Mumbai","pune","Nashik")

#==============================================================================================================

#WAP for menu driven code
# import sys
# def add():
#     val1=int(input("Enter the value of val1 :"))
#     val2=int(input("Enter the value of val2 :"))
#     print("Add = ",val1+val2)

# def sub():
#     val1=int(input("Enter the value of val1 :"))
#     val2=int(input("Enter the value of val2 :"))
#     print("Sub = ",val1-val2)

# def mul():
#     val1=int(input("Enter the value of val1 :"))
#     val2=int(input("Enter the value of val2 :"))
#     print("Mul = ",val1*val2)

# def div():
#     val1=int(input("Enter the value of val1 :"))
#     val2=int(input("Enter the value of val2 :"))
#     print("Div = ",val1/val2)

# while True:
#     print("1.Addition")
#     print("2.Substraction")
#     print("3.Multiplication")
#     print("4.Division")
#     print("5.Exit")
#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         add()
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()
#     elif choice == 5:
#         sys.exit("you now exit")


#-------------------------------------------------------------------------------------------------------------
# 1.rstrip()==>To remove spaces at right hand side
# 2.lstrip()==>To remove spaces at left hand side
# 3.strip()==>To remove spaces both sides

# programming = input("Enter your programming Name : ")
# p_name = programming.rstrip()
# if p_name == 'Python':
#     print(p_name)
# elif p_name=='Java':
#     print(p_name)
# elif p_name=='Cpp':
#     print(p_name)
# else:
#     print("Wrong progrmming name")

#-------------------------------------------------------------------------------------------------------------
