#------------------------Nested For loop---------------------------
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#-------------------------------------------------------------------------------------------------------
# n = int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(j,end=" ")
#     print() 

#--------------------------------------------------------------------------------------------------------
# n = int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(chr(64+i),end=" ")            #chr() is used for typecasting 
#     print()

#-------------------------------------------------------------------------------------------------------

# n = int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()

#-------------------------------------------------------------------------------------------------------
# n = int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()

#---------------------------------------------------------------------------------------------------------
# import time
# n = int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         time.sleep(1)
#         print(n+1-i,end=" ")
#     print()

#--------------------------------------------------------------------------------------------------------
# import time
# n = int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(0.5)
#         print("*",end=" ")
#     print()

#------------------------------------------------------------------------------------------------------