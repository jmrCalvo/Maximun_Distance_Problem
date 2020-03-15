def calculate_sum(matrix, vector):
    pos_i=int(vector[0])
    sum_all=0
    for pos_j in vector:
        sum_all=sum_all+matrix[int(pos_i)][int(pos_j)]
        pos_i=pos_j
    return sum_all
