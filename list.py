# list1 = [3,5,6,]
# print(list1)

matrix = [[1,3,4],
          [4,0,6],
          [6,7,9]]

for row in matrix:
    print(row)

print(matrix)
print(matrix[1][1])
print(matrix[0])

axis = []
for i in range(3):
    row = []
    for x in range(3):
        row.append(0)

    axis.append(row)    
print(axis)
for i in axis:
    print(i)

 #fill a 2d list using inputs

print("fill a 2d list using number you think of")   

ios = []




for z in range(3):
    row = []
    for i in range(3):
        a1 = int(input("enter a number: "))
        row.append(a1)
    ios.append(row)

print(ios)    

#find the biggest number in the matrix
matrix = [[4,5,6],
          [4,8,9],
          [8,3,4]]

max_value = matrix[0][0]
max_row = 0
max_col = 0

for i in range(3):
    for y in range(3):
        if matrix[i][y] > max_value:
            max_value = matrix[i][y]
            max_row = i
            max_col = y

print("Maximum value: ", max_value)    
print("Position (row, column: )", max_row, max_col)
