import galois
from sympy import symbols, gcd, Poly, gcd, rem, divisors, GF, div, LM, degree
import numpy as np

def circulant(a):
	"""Create a landscape matrix of size m x m where the i-th row is the i-th left shift of a"""
	m = len(a)
	result_matrix = np.zeros((m,m), dtype = int)
	for i in range(m):
		result_matrix[i, :] = np.roll(a,i)
	return result_matrix
def portrait(a,n):
	matrix = circulant(a)
	result_matrix = np.delete(matrix, -1, axis=1)
	return result_matrix

def landscape(a,n):
	matrix = circulant(a)
	result_matrix = np.delete(matrix, -1, axis = 0)
	return result_matrix

def mul(f,g):
	GF = galois.GF(2)
	f = galois.Poly(f, field = GF)
	g = galois.Poly(g, field = GF)
	
	result = f * g
	return result
def compute_modulo_binary_field(f, g):
    GF = galois.GF(2)
    f = galois.Poly(f, field=GF)
    g = galois.Poly(g, field=GF)

    result = f % g

    return result
    
def extended_gcd_over_GF2(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, s, t = extended_gcd_over_GF2(b, rem(a, b, domain = 'GF(2)'))
        q, r = div(a,b, domain = 'GF(2)')
        return (d, t, s - t * r)    
    
def return_coeffs(a, p, m):
	res = rem(a,p, domain = 'GF(2)').all_coeffs()
	res.reverse()
	while len(res) < m:
		res.append(0)
	return res
def matrix_rep(a):
	res = np.zeros((4,4))
	res[0] = np.mod(a,2)
	res[1] = np.mod([a[3], a[0] + a[3], a[1] + a[3], a[2] + a[3]],2) 
	res[2] = np.mod([a[2] + a[3], a[2], a[0] + a[2], a[1] + a[2]],2)
	res[3] = np.mod([a[1] + a[2], a[1] + a[3], a[1], a[0] + a[1]],2) 
	return res
