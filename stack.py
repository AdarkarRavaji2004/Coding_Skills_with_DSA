# import sys
# class Stack:
#     def __init__(self):
#        self.stackList = []  # stack created

#     def push(self, value):
#         self.stackList.append(value)  # add element in stack

#     def displayStack(self):
#         print("-------------------------")
#         print(self.stackList)  # display stack
#         print("-------------------------")
    
#     def isEmpty(self):
#         if self.stackList == []:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty, cannot pop element")
#         else:
#             return self.stackList.pop()  # remove element from stack
        
#     def deleteStack(self):
#         self.stackList = []  # delete stack by reassigning empty list
#         return "Stack is deleted"
    
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty, cannot peek element")
#         else:
#             return self.stackList[-1]  # return top element of stack without removing it


# stackObj  = Stack()
# while True:
#     print("=============================")
#     print("1. Push Element in Stack : ")
#     print("2. Display Stack : ")
#     print("3. Check isEmpty : ")
#     print("4. Pop Element from Stack : ")
#     print("5. Delete Stack : ")
#     print("6. Peek Element from Stack : ")
#     print("7. Exit : ")

#     choice = int(input("Enter Your Choice : "))
#     if choice == 1:
#         val = int(input("Enter a value to push in stack : "))
#         stackObj.push(val)
#     elif choice == 2:
#         stackObj.displayStack()
#     elif choice == 3:
#         print("Check isEmpty : ",stackObj.isEmpty())
#     elif choice == 4:
#         print("Popped element is : ",stackObj.pop())
#     elif choice == 5:
#         print(stackObj.deleteStack())
#     elif choice == 6:
#         print("Top element of stack is : ",stackObj.peek()) 
#     elif choice == 7:
#         sys.exit()
#     else:
#         print("Invalid Choice!")

#============================================================================================
#Stack Implementation with size limit

# import sys
# class Stack:
#     def __init__(self, size):
#         self.size = size
#         self.stackList = []  # stack created

#     def isFull(self):
#         if len(self.stackList) == self.size:
#             return True
#         else:
#             return False
        
#     def push(self, value):
#         if self.isFull():
#             print("Stack is full, cannot push element")
#         else:
#             self.stackList.append(value)  # add element in stack

#     def displayStack(self):
#         print("-------------------------")
#         print(self.stackList)  # display stack
#         print("-------------------------")
    
#     def isEmpty(self):
#         if self.stackList == []:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty, cannot pop element")
#         else:
#             return self.stackList.pop()  # remove element from stack
        
#     def deleteStack(self):
#         self.stackList = []  # delete stack by reassigning empty list
#         return "Stack is deleted"
    
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty, cannot peek element")
#         else:
#             return self.stackList[-1]  # return top element of stack without removing it


# size = int(input("Enter the size of stack : "))
# stackObj  = Stack(size)

# while True:
#     print("=============================")
#     print("1. Push Element in Stack : ")
#     print("2. Display Stack : ")
#     print("3. Check isEmpty : ")
#     print("4. Pop Element from Stack : ")
#     print("5. Delete Stack : ")
#     print("6. Peek Element from Stack : ")
#     print("7. Exit : ")

#     choice = int(input("Enter Your Choice : "))
#     if choice == 1:
#         val = int(input("Enter a value to push in stack : "))
#         stackObj.push(val)
#     elif choice == 2:
#         stackObj.displayStack()
#     elif choice == 3:
#         print("Check isEmpty : ",stackObj.isEmpty())
#     elif choice == 4:
#         print("Popped element is : ",stackObj.pop())
#     elif choice == 5:
#         print(stackObj.deleteStack())
#     elif choice == 6:
#         print("Top element of stack is : ",stackObj.peek()) 
#     elif choice == 7:
#         sys.exit()
#     else:
#         print("Invalid Choice!")

#============================================================================================
#Tower of Hanoi

# import time

# class TowerOfHanoi:
#     def __init__(self, source):
#         self.A = source[:]   # source
#         self.B = []          # auxiliary
#         self.C = []          # destination
#         self.n = len(source)

#     def display(self):
#         print(f"A: {self.A}   B: {self.B}   C: {self.C}")
#         print("-" * 40)
#         time.sleep(1)  # delay (1 second)

#     def move_disk(self, from_rod, to_rod, from_name, to_name):
#         if not from_rod:
#             disk = to_rod.pop()
#             from_rod.append(disk)
#             print(f"Move disk {disk} from {to_name} → {from_name}")
#         elif not to_rod:
#             disk = from_rod.pop()
#             to_rod.append(disk)
#             print(f"Move disk {disk} from {from_name} → {to_name}")
#         elif from_rod[-1] > to_rod[-1]:
#             disk = to_rod.pop()
#             from_rod.append(disk)
#             print(f"Move disk {disk} from {to_name} → {from_name}")
#         else:
#             disk = from_rod.pop()
#             to_rod.append(disk)
#             print(f"Move disk {disk} from {from_name} → {to_name}")

#         self.display()  # show state after every move

#     def solve(self):
#         print("Initial State:")
#         self.display()

#         s, a, d = 'A', 'B', 'C'

#         if self.n % 2 == 0:
#             a, d = d, a

#         total_moves = 2 ** self.n - 1

#         for i in range(1, total_moves + 1):
#             if i % 3 == 1:
#                 self.move_disk(self.A, self.C, s, d)
#             elif i % 3 == 2:
#                 self.move_disk(self.A, self.B, s, a)
#             else:
#                 self.move_disk(self.B, self.C, a, d)

#         print("Final State:")
#         self.display()


# # Run
# hanoi = TowerOfHanoi([3, 2, 1])
# hanoi.solve()     


#============================================================================================

import time
class Tower:
    def __init__(self, source):
        print("Welcome to Tower of Hanoi Game!")
        print()
        print("Given Problem     A=[3, 2, 1]   B=[]   C=[]")
        print()
        print("Expected Output   A=[]   B=[]   C=[3, 2, 1]")
        self.A = []   
        self.B = []         
        self.C = []          

    def tower(self,item):
        self.A.append(item)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A)
        print("Items in Tower A\n" )

    def pass1(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass One Completed==========================" )

    def pass2(self):
        self.temp = self.A.pop()
        self.B.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Two Completed==========================" )

    def pass3(self):
        self.temp = self.C.pop()
        self.B.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Three Completed==========================" )

    def pass4(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Four Completed==========================" )

    def pass5(self):
        self.temp = self.B.pop()
        self.A.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Five Completed==========================" )

    def pass6(self):
        self.temp = self.B.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Six Completed==========================" )

    def pass7(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Seven Completed==========================" )
    
obj = Tower([3,2,1])
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()

    