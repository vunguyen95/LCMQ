import utils as utils
import numpy as np
from itertools import product

def generate_binary_vectors(n):
    return list(product([0, 1], repeat=n))
m = 5
n= 4 
b_arr = [[0,1,0,0,1], [0,1,1,0,1], [1,1,1,1,0], [1,0,0,0,0], [1,1,1,0,0]]
#b4 = [1,1,1,0,0]
z_arr = [[1,0,0,0], [0,1,1,1], [0,1,1,1], [0,0,0,1], [1,0,0,1]]
#z4 = , [1,0,0,1]
v = [0,1,0,0,	0,0,0,0,	0,0,0,0,	1,0,0,0,	0,0,0,0]
#v4 = 0000
k = [0,1,1,1,1,0,1,1,0]
min_weight = 21
weights = np.zeros(21)
solutions = []
zero = np.zeros(n+m, dtype = int)
B0 = utils.portrait(b_arr[0],n)
B1 = utils.portrait(b_arr[1],n)
B2 = utils.portrait(b_arr[2],n)
B3 = utils.portrait(b_arr[3],n)
B4 = utils.portrait(b_arr[4],n)
Z0 = utils.matrix_rep(z_arr[0])
Z1 = utils.matrix_rep(z_arr[1])
Z2 = utils.matrix_rep(z_arr[2])
Z3 = utils.matrix_rep(z_arr[3])
Z4 = utils.matrix_rep(z_arr[4])
B  = np.hstack((B0, B1, B2,B3, B4))
Z = np.hstack((Z0,Z1,Z2,Z3, Z4))
M = np.vstack((Z,B))
print(M)
print(np.dot(k,M) % 2)


	
#print(utils.portrait(b[0], n))

#print(utils.portrait(b[1], n))

#print(utils.portrait(b[2], n))

#print(utils.portrait(b[3], n))
print(v)

vectors = generate_binary_vectors(n+m)
for vector in vectors:
	
	if(np.array_equal(vector,zero) == False):
	
		test = np.dot(vector,M) % 2
		weight = np.count_nonzero(test)
		weights[weight] += 1
		if weight == 2:
			print("Weight 2", vector)
		if weight < min_weight:
			min_weight = weight
			solution = vector

print(min_weight)
print(solution)
print(weights)

	
