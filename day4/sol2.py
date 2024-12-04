from read_input import read_input

# Brute force solution

A = read_input("input.txt")

# Array dimensions
N, M = len(A), len(A[0])

# Target = MAS

# Done
def left_side(i, j):
    return A[i-1][j-1] == 'M' and A[i+1][j-1] == 'M' and A[i-1][j+1] == 'S' and A[i+1][j+1] == 'S'


# x
def right_side(i, j):
    return A[i-1][j+1] == 'M' and A[i+1][j+1] == 'M' and A[i-1][j-1] == 'S' and A[i+1][j-1] == 'S'

# x
def top_side(i, j):
    return A[i-1][j-1] == 'M' and A[i-1][j+1] == 'M' and A[i+1][j-1] == 'S' and A[i+1][j+1] == 'S'

# x
def bottom_side(i, j):
    return A[i+1][j-1] == 'M' and A[i+1][j+1] == 'M' and A[i-1][j-1] == 'S' and A[i-1][j+1] == 'S'


sum = 0
for i in range(1,N-1):
    for j in range(1,M-1):
        if A[i][j] == 'A':
            sum += int(left_side(i,j) or right_side(i,j) or top_side(i,j) or bottom_side(i,j))


print(sum)