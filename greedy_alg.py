import numpy as np

def algorythm(no_solutions,matrix,init_number):
    solution=np.zeros(no_solutions)
    index=no_solutions
    solution[0]=init_number
    while no_solutions != 1:
        t=int(np.argmax(matrix[int(index)-int(no_solutions)]))
        solution[int(index)-int(no_solutions)+1]=t
        matrix[:,t]=0
        matrix[t,:]=0
        no_solutions=no_solutions-1
    return solution
        
