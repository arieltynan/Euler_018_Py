# Euler Problem 018
# Solved 24 January 2021

# Maximum path sum I

def compare(row,col):
    if matrix[row-1,col-1] > matrix[row-1,col]:
        return (matrix[row-1,col-1] + matrix[row,col])
    else:
        return (matrix[row-1,col] + matrix[row,col])

grid = str("""75 
95 64 
17 47 82 
18 35 87 10 
20 04 82 47 65 
19 01 23 75 03 34 
88 02 77 73 07 63 67 
99 65 04 28 06 16 70 92 
41 41 26 56 83 40 80 70 33 
41 48 72 33 47 32 37 16 94 29 
53 71 44 65 25 43 91 52 97 51 14 
70 11 33 28 77 73 17 78 39 68 17 57 
91 71 52 38 17 14 91 43 58 50 27 29 48 
63 66 04 68 89 53 67 30 73 16 69 87 40 31 
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".replace("\n",""))

#Replicate triangle with 2D matrix
grid = grid.split() #split into indvidual strings
for i in range(0, len(grid)): #convert str to int
    grid[i] = int(grid[i])

w, h = 15, 15
matrix = { (i,j):0 for i in range(w) for j in range(h) }
ind = 0
for i in range(1,h + 1): #row position
    for j in range(1,i + 1): #col position
        matrix[i,j] = grid[ind]
        ind = ind + 1

#for i in range(0,h):
#        print(matrix[1])
# for i in range(1,h+1):
#    for j in range(1,i+1):
#        print(matrix[i,j], end=" ")
#    print("")

n = w
for rownum in range(1,n):
    matrix[rownum+1,1] = matrix[rownum+1,1] + matrix[rownum,1]
    matrix[rownum+1,rownum+1] = matrix[rownum+1,rownum+1] + matrix[rownum,rownum]
for i in range(2,h+1):
    for j in range(2,i+1):
        if i != j and i > 2:
            matrix[i,j] = compare(i,j)

tot = 0
i = 1
while i < n + 1:
    if matrix[n,i] > tot:
        tot = matrix[n,i]
    i = i + 1
print(tot)   

