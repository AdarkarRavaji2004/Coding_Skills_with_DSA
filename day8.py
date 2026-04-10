#Input :
#3 4
#100 198 333 323
#122 232 221 111
#223 565 245 764

#Output :
#333 232 764

# m = int(input("Enter number of days: "))
# n = int(input("Enter number of products: "))

# matrix = []

# for i in range(m):
#     print("Enter elements for row", i + 1)
#     row = []

#     for j in range(n):
#         value = int(input(f"Enter element at position [{i}][{j}]: "))
#         row.append(value)

#     matrix.append(row)

# print("Matrix:")
# for row in matrix:
#     print(row)

# print("Highest sales:")

# for row in matrix:
#     print(max(row),end=" ")

#========================================================================

#write a function to remove leading zeros from a list of integers
#sample input = [0,0,1,2,0,3,0,0,4]
#Expected utput = [1,2,0,3,0,0,4]

s = [0,0,1,2,0,3,0,0,4]
result = []
started = False

for num in s:
    if num != 0:
        started = True
    if started:
        result.append(num)

print(s)
print(result)