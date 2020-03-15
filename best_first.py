import read_file
import sys
import random
import objective
import numpy as np
import greedy_alg
from time import time
import blockElements
import threading

OBJETIVECOUNT=0


def calculateNeighboursWeights(matrix,initial_pos,forbiddenElements,n_solutions):
    neighbours=np.arange(matrix[0].size)
    neighboursWay=[None] * matrix[0].size
    copyMatrix=np.array(matrix)
    copyMatrix=blockElements.block(forbiddenElements,copyMatrix)

    for index in range(matrix[0].size):
        
        # if OBJETIVECOUNT >100000:
        #     print("MORE THAN 100000 CALCULATIONS OF OBJETIVE")
        #     break
        if index in forbiddenElements:
            #print("++++++++++esta prohibido",index)
            neighbours[index]=0
            neighboursWay[index]=[]
        else:
            #print("**********esta posible",index)
            forbiddenElements=np.append(forbiddenElements,initial_pos)
            #way=greedy.createSolution(index,copyMatrix,n_solutions)
            way=greedy_alg.algorythm(n_solutions,copyMatrix,index)
            neighboursWay[index]=np.insert(way,0,initial_pos)
            neighbours[index]=objective.calculate_sum(matrix,neighboursWay[index])
            global OBJETIVECOUNT
            OBJETIVECOUNT=OBJETIVECOUNT+1

    return(neighbours,neighboursWay)
    

def createAlternativeSolution(positionValue,matrix,forbiddenElements,oldSolution):
    copyMatrix=np.array(matrix)
    (neighbours,neighboursway)=calculateNeighboursWeights(copyMatrix,positionValue,forbiddenElements,oldSolution.size)
    maximIndex=np.argmax(neighbours)
    
    return (neighbours[maximIndex],neighboursway[maximIndex])


def createSolution(initial,matrix,noSolutions):
    global OBJETIVECOUNT
    OBJETIVECOUNT=0

    #solutionActual=greedy.createSolution(initial,matrix,noSolutions)
    solutionActual=greedy_alg.algorythm(noSolutions,matrix,initial)

    #the index is from the start until the length of the array minus one,
    #because the last movement to be changed is the minus two with can
    #select just the maximun
    
    for index in range(len(solutionActual)-2):
        oldWeight=objective.calculate_sum(matrix,solutionActual[index:])
        OBJETIVECOUNT=OBJETIVECOUNT+1
        
        (weight,neighboursway)=createAlternativeSolution(solutionActual[index],matrix,solutionActual[:index],solutionActual[index+1:])
        if(weight>oldWeight):
            solutionActual=np.concatenate((solutionActual[:index], neighboursway))
        if OBJETIVECOUNT >100000:
            break
    return solutionActual



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
    solution = createSolution(init,matrix,n_solutions)
    elapsed_time = time() - start_time


    print(solution)
    print(objective.calculate_sum(matrix,solution))
    print("el tiempo fue",elapsed_time)



OBJETIVECOUNT=0

if __name__ =="__main__":
    main()

