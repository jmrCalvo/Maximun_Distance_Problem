import numpy as np

def initialize_matrix(length):
    array=np.zeros((int(length), int(length))) 
    return array

def create_array(fileName):
    with open(fileName) as my_file:
        first_line=my_file.readline()
        matrix = initialize_matrix(first_line.split()[0])
        for line in my_file:
            matrix[int(line.split()[0])][int(line.split()[1])]=float(line.split()[2])
            matrix[int(line.split()[1])][int(line.split()[0])]=float(line.split()[2])
            
    return (matrix, int(first_line.split()[1]))


