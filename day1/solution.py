import math
# Read the file and process the input
with open("input1.txt", "r") as file:  # Replace "input.txt" with your filename
    lines = file.readlines()

# Split the lines into two lists
list1, list2 = zip(*(map(int, line.split()) for line in lines))

# Convert to regular Python lists if needed
list1 = list(sorted(list1))
list2 = list(sorted(list2))

diff = 0

for x,y in zip(list1,list2):
    diff += abs(x-y)

print(diff)
