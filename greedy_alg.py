import numpy as np
def nextElemnt(selected_elements,possible_elements ):
    possible_elements_copy = np.array(possible_elements, copy=True)
    solution=int(np.argmax(possible_elements_copy))
    if solution in selected_elements :
        possible_elements_copy[solution]=0
        return nextElemnt(selected_elements,possible_elements_copy)
    else :
        return solution

def algorythm(no_solutions,matrix,init_number):
    solution=np.arange(no_solutions)
    index=no_solutions
    solution[0]=init_number
    while no_solutions != 1:
        t=nextElemnt(solution,matrix[int(index)-int(no_solutions)])
        solution[int(index)-int(no_solutions)+1]=t
        no_solutions=no_solutions-1
    return solution
        
