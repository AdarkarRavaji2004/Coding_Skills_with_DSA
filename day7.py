#Write a function to sort a dictionary by keys or values in ascending or descending order
#sample input :{"C":3,"B":2,"A":1}
#output-Ascending order :{"A":1,"B":2,"C":3}
#output-Descending order : {"C":3,"B":2,"A":1}

# Dict={"B":2,"A":1,"C":3}
# Asc_key=sorted(Dict.items())
# print(Asc_key)
# Desc_value=sorted(Dict.items(),reverse=True)
# print(Desc_value)

#Remove all Elements from dictionary
#Write a function to remove all elements from a dictionary
#sample input :{"A":1,"B":2,"C":3}
#output : {}

# dict = {"A":1,"B":2,"C":3}
# dict.clear()
# print(dict)

#---------------------------------------------------------------------
#Write a function to count the nuumber of non=empty(non-null) values in a dictionary
#sample input : {"A":1,"B":"","C":3,"D":None,"E":"Five"}

# dict1 = {"A":1,"B":"","C":"3","D":None,"E":"Five"}
# count = 0
# for i in dict1.values():
#     if i:
#         count+=1
# print("Number of non empty values:",count)

#============================================================================================

# def findBiggestNumber(array):
#     biggestNumber = array[0]#================>O(1)
#     for i in range(1, len(array)):#==========>O(n)=====================O(n)
#         if array[i] > biggestNumber:#========>O(1)=========O(1)=======
#             biggestNumber = array[i]#========>O(1)=========
#     return biggestNumber#====================>O(1)

# #O(1)+O(n)+O(1)=O(n)
# array = [2,4,5,6,7,1,9,3,4,5,6]
# result = findBiggestNumber(array)
# print("The biggest number is:", result)

#=============================================================================================
# str = "gasgg54@#vscsd!s*"
# #output = 4
# count = 0
# for i in str:
#     if not i.isalnum():
#         count += 1
# print(count)

#-----------OR----------------------

# var = "gasgg54@#vscsd!s*"
# count = 0
# for i in var:
#     z = ord(i)
#     if z>=97 and z<=122:
#         continue
#     elif z>=48 and z<=57:
#         continue
#     else:
#         count+=1
# print(count)

#---------------------------------------------------------------------------------------------
#input = 79,77,54,81,48,34,25,16
#output = 3
# The areas that are in square form are 81,25 and 16,So output is 3

# list = [79,77,54,81,48,34,25,16]
# count = 0
# for i in list:
#     if int(i**0.5)**2 == i:
#         count += 1
# print(count)

#---------------OR----------------------

# import math
# a = [79,77,54,81,48,34,25,16]
# count = 0
# for i in a:
#     if math.sqrt(i) == math.sqrt(i)//1:
#         count+=1
# print("The total square plots are:",count)

#---------------------------------------------------------------------------------------------

