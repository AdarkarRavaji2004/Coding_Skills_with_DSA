#-------------------------Dictionary-------------------------------------

# mydict = {
#     101 : "prashant",
#     102 : "ashish",
#     "103" : "mohini",
#     "104" : "trivani",
#     101 : "ashish",
#     104 : "ashish"
# }
# print(mydict)

# #remove key and value
# mydict.pop(101)
# print(mydict)

#with the help of key we have to print the values
# a = mydict[102]
# print(a)

#We will replace old value by new value
# mydict[102] = "peter"
# print(mydict)

#Only print the keys x=0,1
# for x in mydict:
#     print(x)

#Only print the values
# for x in mydict.values():
#     print(x)

#printing key and value both
# for x,y in mydict.items():
#     print(x, y)

#if i have to add new key and value pair in my dictionary
# mydict["mobile_no"]=4628561953
# print(mydict)

# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])


# a ={'a':1,'b':2,'c':3}
# print(a['a','b']) #we cannot retrieve value using two key in same bracket

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] +=1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)

#---------------------------------------------------------------------------------------------------------

# mydict = {}
# mydict[1] = 1
# mydict['1'] = 2
# mydict[1.0] = 4
# print(mydict)

# sum = 0
# for k in mydict:
#     sum += mydict[k]
# print(sum)

#--------------------------------------------------------------------------

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum= 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)

#----------------------------------------------------------

# box = {}
# jars = {}
# creates = {}
# box['biscuit'] =1
# box['cake'] =3
# jars['jam'] =4
# creates['box'] = box
# creates['jars'] = jars
# print(len(creates[box]))        #TypeError

#------------------------------------------------------

# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])

#-----------------------------------------------------

# rec = {"Name" : "python","Age":"20"}
# r=rec.copy()
# print(id(r) == id(rec))
# print(id(rec))
# print(id(r))

#------------------------------------------------------

# rec = {"Name" : "python","Age":"20"}
# id1 = id(rec)
# print(id(rec))
# del rec

# rec = {"Name" : "python","Age":"20"}
# id2 = id(rec)
# print(id(rec))
# print(id1 == id2)

#---------------------------

#Write a function to find the key with the minimum value in the dictionary
# dict = {"x":20,"y":10,"z":30}
# min = ''
# for i in dict.items():
    
#     if :
#         p = 
    

#