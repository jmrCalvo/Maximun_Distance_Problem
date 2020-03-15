import read_file
import sys
import random
import objective
import numpy as np
import blockElements
from time import time


def createSolution(init,matrix,n_solutions, forbiddenElements=[]):
    totalSize=n_solutions
    copyMatrix=np.array(matrix)
    #this is done to verify that there is nothing on the black list before to run
    #this code correctly
    copyMatrix=blockElements.block(forbiddenElements,copyMatrix)
    solution=np.arange(n_solutions)
    solution[0]=init
    actualValue=init
    while(n_solutions>1):
        #set the variable of position
        beforePos=totalSize-n_solutions
        actualPos=beforePos+1
        #get the position of the higher value
        actualValue=np.argmax(copyMatrix[actualValue])
        #add the solution to the vector
        solution[actualPos]=actualValue
        #the before element selected will be blocked 
        copyMatrix=blockElements.block([solution[beforePos]],copyMatrix)

        n_solutions=n_solutions-1
    return solution

def main():
    #the initial
    SEED = int(sys.argv[1])
    file=str(sys.argv[2])
    #read of the file
    matrix,n_solutions = read_file.create_array(file)

    #create the init element
    random.seed(SEED)
    init=random.randint(0,matrix[0].size)

    start_time = time()
    solution=createSolution(init,matrix,n_solutions)
    elapsed_time = time() - start_time

    print("el costo es",objective.calculate_sum(matrix,solution))
    print("el tiempo fue",elapsed_time)

if __name__ =="__main__":
    main()

