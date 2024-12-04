def read_input(file_name):
    with open(file_name, 'r') as file:
        two_d_array = [list(line.strip()) for line in file]
        return two_d_array
