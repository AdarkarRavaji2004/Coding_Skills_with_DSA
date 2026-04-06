# f = open("myfile.txt","w")
# print("name of file :",f.name)
# print("file mode :",f.mode)
# print("readable :",f.readable())
# print("writable :",f.writable())
# print("file closed :",f.closed)
# f.close()
# print("file closed :",f.closed)

#---------------------------------------------------------------------------
#performing write operation
# f = open("myfile.txt","w")
# f.write("Pune is a smart city")
# f.close()
# print("File operation is done")

# #perform append operation
# f = open("myfile.txt","a")
# f.write("\n nagpur is a smart city")
# f.close()
# print("File operation is done")

#inserting list

# f = open("newfile.txt","w")
# mylist = ["ravaji","parshuram","adarkar"]
# f.writelines(mylist)
# f.close()
# print("written work has done successfully")]

#read data from a file
# f = open("myfile.txt","r")
# print(f.read())
# f.close()

# #with statement
# with open("textfile.txt","w") as f:
#     f.write("Amit\n")
#     f.write("Ashish\n")
#     f.write("Prashant\n")
#     print("file closed :",f.closed)
# print("file closed :",f.closed)

# with open("textfile.txt","r") as f:
#     content = f.read()
#     print(content)

#binary file
# f1 = open("cartoon.jpg","rb")
# f2 = open("Tom.jpg","wb")
# data = f1.read()
# f2.write(data)
# print("New Image is available with the name...")

#---------------------------------------------------------------------------------

# import csv
# f = open("student.csv","a",newline="")
# a = csv.writer(f)
# # a.writerow(["studentID","rollNo","name","mobileNo"])

# studentid = input("Enter student Id :")
# rollno = input("Enter student roll no :")
# name = input("Enter your name :")
# mobileno = int(input("Enter Mobile Number :"))
# a.writerow([studentid,rollno,name,mobileno])
# print("student record has save...")

#--------------------------------------------------------------------------------
import csv
f = open("record.csv","a")
a = csv.writer(f)
a.writerow(["RollNo","Name","MobileNo","Email","P1","P2","P3","Total","Percentage","Result"])

rollno=input("Enter your Roll No :")
name = input("Enter your name :")
mobileno =input("Enter your Mobile No :")
email = input("Enter your Email id :")
p1 =int(input("Enter mark of Sub 1 :"))
p2 =int(input("Enter mark of Sub 2 :"))
p3 =int(input("Enter mark of Sub 3 :"))
total = p1+p2+p3
percentage = total/3.0
if p1 >= 40 and p2 >= 40 and p3 >= 40:
    result = "Pass"
else:
    result = "Fail"

a.writerow([rollno,name,mobileno,email,p1,p2,p3,total,percentage,result])
print("Saved Record Successfully...")