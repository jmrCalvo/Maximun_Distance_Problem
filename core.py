import read_file, greedy_alg,best_first,objective
import random
from time import time
import sys
import numpy as np
import sys
sys.setrecursionlimit(10**8)

FILES=['./examples/GKD-c_11_n500_m50.txt','./examples/GKD-c_12_n500_m50.txt','./examples/GKD-c_13_n500_m50.txt', './examples/GKD-c_14_n500_m50.txt',
'./examples/GKD-c_15_n500_m50.txt', './examples/GKD-c_16_n500_m50.txt', './examples/GKD-c_17_n500_m50.txt','./examples/GKD-c_18_n500_m50.txt',
'./examples/GKD-c_19_n500_m50.txt', './examples/GKD-c_20_n500_m50.txt','./examples/MDG-a_31_n2000_m200.txt','./examples/MDG-a_32_n2000_m200.txt', './examples/MDG-a_33_n2000_m200.txt',
'./examples/MDG-a_34_n2000_m200.txt', './examples/MDG-a_35_n2000_m200.txt','./examples/MDG-a_36_n2000_m200.txt','./examples/MDG-a_37_n2000_m200.txt',
'./examples/MDG-a_38_n2000_m200.txt', './examples/MDG-a_39_n2000_m200.txt', './examples/MDG-a_40_n2000_m200.txt', 
'./examples/MDG-b_1_n500_m50.txt','./examples/MDG-b_2_n500_m50.txt','./examples/MDG-b_3_n500_m50.txt','./examples/MDG-b_4_n500_m50.txt', './examples/MDG-b_5_n500_m50.txt',
'./examples/MDG-b_6_n500_m50.txt', './examples/MDG-b_7_n500_m50.txt','./examples/MDG-b_8_n500_m50.txt','./examples/MDG-b_9_n500_m50.txt',
'./examples/MDG-b_10_n500_m50.txt'
 ]
#calculate the sum of the distances selected in the array



SEED = int(sys.argv[1])

for file in FILES:
    matrix,n_solutions = read_file.create_array(file)
    random.seed( SEED+1 )
    SEED=SEED+1

    #Choose the random number
    init=random.randint(0,500)
    

    start_time_greedy = time()
    arr_greedy=greedy_alg.algorythm(n_solutions,matrix,init)
    elapsed_time_greedy = time() - start_time_greedy

    print("el array de greedy de ",file," es ", arr_greedy)
    print("el tiempo de greedy de ",file," es ",elapsed_time_greedy)
    print("el costo de greedy de ",file," es ", objective.calculate_sum(matrix,arr_greedy))


    start_time_BL = time()
    arr_BL=best_first.createSolution(init,matrix,n_solutions)
    elapsed_time_BL = time() - start_time_BL

    print("el array de BL de ",file," es ", arr_BL)
    print("el tiempo de BL de ",file," es ",elapsed_time_BL)
    print("el costo de BL de ",file," es ", objective.calculate_sum(matrix,arr_BL))
    
    print("\n\n")