import numpy as np
import greedy_alg
import random

def calculate_sum(matrix, vector):
    pos_i=vector[0]
    sum_all=0
    for pos_j in vector:
        sum_all=sum_all+matrix[int(pos_i)][int(pos_j)]
        pos_i=pos_j
    return sum_all


def isBetter(new_array,old_array,matrix):
    if calculate_sum(matrix,new_array)>calculate_sum(matrix,old_array) :
        return True
    else:
        return False

def calculateNeighbours(vector, initial_pos):
    size=len(vector)
    return [x for x in range(initial_pos, initial_pos+size)]

def calculateMatrix(forbiddenelements, matrix):
    copymatrix=np.array(matrix)
    for elements in forbiddenelements:
        copymatrix[:][elements]=-1
        copymatrix[elements][:]=-1
    return copymatrix


def calculateNeighboursWeights(vector, matrix,noElements, notPossible):
    weigthSolution=np.arange(len(vector))
    for index in range(0, len(vector)-1):
        if vector[index] in notPossible:
            weigthSolution[index]=0
        else:
            copymatrix=np.array(matrix)
            partialSolution=greedy_alg.algorythm(noElements,copymatrix,vector[index])
            weigthSolution[index]=calculate_sum(matrix,partialSolution)
    return weigthSolution


def createSolution(solution,matrix,tries):
    #print(solution)
    actualSolution=np.array(solution)

    for index in range(0,len(solution)-1):
        copymatrix=calculateMatrix(solution[:index-1],matrix)
        #print("los seleeeeeccionas son ",len(solution)-1,"y el indice es ", index)
        selected=solution[index]
        #print("los seleeeeeccionas son",selected)
        #print(solution[index])
        #print("not possibles",solution[:index+1] )
        neighbours=matrix[selected][selected+1:]
        if len(neighbours) != 0:
            #print("los vecinos son", calculateNeighbours(neighbours, selected+1))
            neighboursWeight=calculateNeighboursWeights(calculateNeighbours(neighbours, selected+1), copymatrix,len(solution)-(index+1),solution[:index+1])  
            #print("los vecinos son",calculateNeighboursWeights(calculateNeighbours(neighbours, selected+1), copymatrix,len(solution)-(index+1),solution[:index+1]))   
            #print("el maximo valor es ", np.amax(neighboursWeight))
            maxim=np.amax(neighboursWeight)
            #print("el indice es ", int(np.argwhere(neighboursWeight == int(maxim))))
            result=np.argwhere(neighboursWeight == np.amax(neighboursWeight))

            if maxim > calculate_sum(matrix,solution[index:]):
                partialsolution=solution[:index]
                #solution[index:]=greedy_alg.algorythm(len(solution)-(index+1),copymatrix,result[0][0])
                #print("*********************************************************************** SE HA CAMBIADOOOOOOOO")
                #print("esta es la solucion actual", solution)
                #print("esta es la solucion parcial", partialsolution)
                newPartialSoluion=greedy_alg.algorythm(len(solution)-(index),copymatrix,result[0][0])
                #print("KKKKKKKKKKKKKKKKKKKKKKKKKK", partialsolution)
                #print("TTTTTTTTTTTTTTTTTTTTTTTTTT", solution[index:])
                #print("SSSSSSSSSSSSSSSSSSSSSSSSSS",newPartialSoluion)
                #print("esta es la solucion que se le va añadir", greedy_alg.algorythm(len(solution)-(index+1),copymatrix,result[0][0]))
                solution=np.concatenate((partialsolution, newPartialSoluion))

    if isBetter(solution,actualSolution,matrix):
        return solution
    else:
        return actualSolution
    
    #print("el indice es ", result[0][0])
    #print("\n")
    #print("\n\n")


def algorythm(no_solutions,matrix,init_number):
    solution=greedy_alg.algorythm(no_solutions,matrix,init_number)
    #print(solution)
    return createSolution(solution,matrix,0)

    

