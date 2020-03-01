import read_file, greedy_alg
import random

SEED = 0
matrix,n_solutions = read_file.create_array('./examples/GKD-c_11_n500_m50.txt')

random.seed( SEED )
#Choose the random number
init_greedy=random.randint(0,500)

arr=greedy_alg.algorythm(n_solutions,matrix,init_greedy)
print arr