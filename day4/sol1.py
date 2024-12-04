from read_input import read_input

# Brute force solution

array = read_input("input.txt")

# Array dimensions
N, M = len(array), len(array[0])

target = "XMAS"

# Left -> Right

# i = row, j = col
def left_to_right_search(A, i, j):
    if j+3 >= M:
        return False
    else:
        return A[i][j] == 'X' and A[i][j + 1] == 'M' and A[i][j+2] == "A" and A[i][j+3] == "S"
        
# Right -> Left
def right_to_left_search(A, i, j):
    if j-3 < 0:
        return False
    else:
        return A[i][j] == 'X' and A[i][j - 1] == 'M' and A[i][j-2] == "A" and A[i][j-3] == "S"

# Up -> down
# Right -> Left
def up_down_search(A, i, j):
    if i+3 >= N:
        return False
    else:
        return A[i][j] == 'X' and A[i+1][j] == 'M' and A[i+2][j] == "A" and A[i+3][j] == "S"

# Down -> Up
def down_up_search(A, i, j):
    if i-3 < 0:
        return False
    else:
        return A[i][j] == 'X' and A[i-1][j] == 'M' and A[i-2][j] == "A" and A[i-3][j] == "S"

# Bottom left -> Top right
def up_right_search(A, i, j):
    if i-3 < 0 or j+3 >= M:
        return False
    else:
        return A[i][j] == 'X' and A[i-1][j+1] == 'M' and A[i-2][j+2] == "A" and A[i-3][j+3] == "S"

# Bottom right -> Top left
def up_left_search(A, i, j):
    if i-3 < 0 or j-3 < 0:
        return False
    else:
        return A[i][j] == 'X' and A[i-1][j-1] == 'M' and A[i-2][j-2] == "A" and A[i-3][j-3] == "S"

# Top left -> Bottom right
def down_right_search(A, i, j):
    if i+3 >= N or j+3 >= M:
        return False
    else:
        return A[i][j] == 'X' and A[i+1][j+1] == 'M' and A[i+2][j+2] == "A" and A[i+3][j+3] == "S"
    
# Top right -> Bottom left
def down_left_search(A, i, j):
    if i+3 >= N or j-3 < 0:
        return False
    else:
        return A[i][j] == 'X' and A[i+1][j-1] == 'M' and A[i+2][j-2] == "A" and A[i+3][j-3] == "S"
    

def search(A):

    # Double for loop
    sum = 0

    for i in range(N):
        for j in range(M):

            sum += int(left_to_right_search(A, i, j))
            sum += int(right_to_left_search(A, i, j))
            sum += int(up_down_search(A, i, j))
            sum += int(down_up_search(A, i, j))

            sum += int(up_left_search(A, i, j))
            sum += int(up_right_search(A, i, j))
            sum += int(down_left_search(A, i, j))
            sum += int(down_right_search(A, i, j))

    return sum

print(search(array))