import numpy as np

def block(arrayForbidenElements, matrix):
    copyMatrix=np.array(matrix)
    if len(arrayForbidenElements)==0:
        return matrix
    for element in arrayForbidenElements:
        copyMatrix[:,element]=0
        #copyMatrix[element,:]=0
    return copyMatrix
