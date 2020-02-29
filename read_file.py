import numpy as np

def initialize_matrix(height,width):
    array=np.zeros((int(height), int(height))) 
    return array

def create_array(fileName):
    with open('./examples/GKD-c_11_n500_m50.txt') as my_file:
        first_line=my_file.readline()
        matrix = initialize_matrix(first_line.split()[0],first_line.split()[1])
        for line in my_file:
            matrix[int(line.split()[0])][int(line.split()[1])]=float(line.split()[2])
    return matrix
