# print('prashantjha777'.isalnum())   #True
# print('prashantjha'.isalpha())  #True
# print('777f'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANT'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(''.isspace())
# print('Hello'.startswith("He"))
# print("Hello".endswith("lo"))

# print("Prashant".find("z"))
# print("Prashant".index("t"))
# print("prashant jha".count("a"))

#Write a function to check if a key exists in a dictionary
# myDict = {"name":"alice","age":30}
# key = input("Enter the key name :")

# if key in myDict.keys():
#     print("key is exist")
# else:
#     print("key does not exist")

#write a function to count the frequency of elements in a list using a dictionary
# list = [1,2,2,3,4,3,5]
# dict ={}
# newList = []
# for i in list:
#     if i not in newList:
#         newList+= i
    
# list=[1,2,2,3,4,3,5]
# dict={}
# for i in list:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)


#--------------------------------------------------------------
#Question is in screen shot 
# mylist = [5,7,8,3,7,8,9,2,3]
# newlist = []

# for i in range(len(mylist)):
#     count = 0
#     key = mylist[i]

#     j=i+1
#     while j<len(mylist):
#         if key == mylist[j]:
#             newlist.append(key)
#         j = j+1
# print(len(newlist))

#--------------------------------------------
#Find the second largest Element
# list = [7,3,9,2,8]
# list.sort()
# print(list)
# print(list[-2])

#------------------------------------------------

# i=1
# while i<=5:
#     print(i)
#     i =i+1

#------------------------------------------------------
# username = ""
# password = ""
# while username!="admin" or password!="admin":
#     username=input("Enter Username :")
#     password=input("Enter password :")

#----------------------------------------------------
# name ="programming"
# vowels = ['a','e','i','o','u']
# cons = 0
# vowel = 0
# for i in name:
#     if i in vowels:
#         vowel +=1
#     else:
#         cons+=1
# print("Consonent = ",cons)
# print("Vowels = ",vowel)

#-----------------------------------------------------------------
#Write a function to remove all occurrences of a specific element form a list

# list = [1,2,2,3,4,2]
# new = []
# for i in list:
#     if i != 2:
#         new.append(i)
# print(new)
#-------------------------OR------------------------------

# input = [1,2,2,3,4,2]
# new = []
# newname = []
# for i in input:
#     if i == 2:
#         new.append(i)
#     else:
#         newname.append(i)
# print(new)
# print("The final list is:", newname)


#------------------------------------------------------------------------------------------------
#Write a function to reverse the order of element in a list
# list = [1,2,3,4,5]
# newlist = list[::-1]
# print(newlist)

#Write a finction to check if a list is a palindrome
# mylist = [1,2,3,2,1]
# if mylist == mylist[::-1]:
#     print("Given list is Palindrome")
# else:
#     print("Not a palindrome")

#Write a function to find common elements between two list:
list1 = [1,2,3,4]
list2 = [3,4,5,6]
new = []
for i in list1:
    for j in list2:
        if i == j:
            new.append(i)
        

print(new)