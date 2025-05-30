#A good way to visualize a 2d array is as a list of lists

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0])
print(matrix[1])
print(matrix[2])

print("Another way of this ",end="\n\n\n")

for i in matrix:
    for j in i:
        if j==3 or j==6:
            print(j,end="\n")
        else:
            print(j,"\t",end='')    
    