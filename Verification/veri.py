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
	

m = 5
n = m - 1
x = symbols('x')
p = Poly(x**5 + 1, domain = 'GF(2)')
f = Poly(x**4 + x**3 + x**2 + x + 1, domain = 'GF(2)')
GF = galois.GF(2)



"""---------------------Keys-----------------------------------"""
k1 = Poly(x**3 + x**2 + 1, domain = 'GF(2)')
k1_array = return_coeffs(k1,p,m)
k1_red = rem (k1, f, domain = 'GF(2)')
k1_red_arr = return_coeffs(k1,f,n)
k1_matrix = portrait(k1_array,n)

print("k1(x) = ", k1)
print(k1_matrix)
print("k1 =", return_coeffs(k1,p,m))
print("k1_red:", k1_red)
print("k1_red =", k1_red_arr)

print("-----------------------------------")
k2 = Poly(x**4 + x**2, domain = 'GF(2)')
#k2_array = [0,0,1,0,1]
k2_array = return_coeffs(k2,p,m)
k2_matrix = landscape(k2_array,n)
k2_prime = rem(k2,f,domain = 'GF(2)')
k2_inverse = Poly(x**3 + x**2 + x, domain = 'GF(2)')
k2_inverse_arr = return_coeffs(k2_inverse,f,n)

print("k2(x) = ", k2)
print("k2 = ", k2_array)
print(k2_matrix)

print("k2 stuffs:")
print("k2_prime =",k2_prime)
print("k2_inverse: ", k2_inverse_arr)

#k2_inverse_arr = [0,1,1,1]

"""print("check k2_inverse")
print(gcd(k2_prime, f, domain = 'GF(2)'))
print(rem(k2_prime*k2_inverse, f, domain = 'GF(2)'))
print(k2_prime*k2_inverse)
print(f * Poly(x**2 + 1, domain = 'GF(2)'))"""

print("---------------")



"""----------------------------RANDOMNESS------------------------"""
"""b vector"""
b = Poly(1 + x + x**2, x , domain = 'GF(2)')
#b_array = [0,1,1,0,1]
b_array = return_coeffs(b,p,m)
b_matrix = portrait(b_array,n)
b_red = rem(b, f, domain = 'GF(2)')
b_red_arr = return_coeffs(b,f,n)
print("b(x) = ", b)
print("b = ", b_array)

print("b(x)_red:", b_red)
print("b_red:", b_red_arr)
print("---------------")

"""Noise: length n"""
v = Poly(0,x, domain = 'GF(2)')
v_array = return_coeffs(v, f,n)
print("v(x)=", v)
print("v = ", v_array)

"""----------------------------TAG RESPONSE-------------------------------------"""

print("y and check: ")
y = rem(b * k1 + v, p, domain = 'GF(2)')
y_short = y
""" the polynomial corresponding to y_array is y - LM(y) (without the leading monomial)"""
if degree(y,x) == n:
	y_short = Poly(y - LM(y), domain = 'GF(2)') 
y_array = (np.dot(b_array, k1_matrix) + v_array) %2
print("y(x) = ", y)
print("y(x)_short = ", y_short)
print("y", y_array)
print("originally (without noise),", np.dot(b_array, circulant(k1_array)) % 2)

print("---------------")
print("z and check:")
z = rem(y_short * k2, p , domain = 'GF(2)')
z_array = np.dot(y_array, k2_matrix) % 2
print("z(x) =", z)
print("z =",z_array)
z_red = rem(z,f, domain = 'GF(2)')
print("z(x)_red:", z_red)
z_red_arr = return_coeffs(z_red, f, n)
print("z_red", z_red_arr)
 

#print(rem(y,p))




"-----------------------CHECKING MATRIX------------------------------------"



print("---------------")
print("check z_red*k2_inverse Mod X^m-1 + ... + 1 = y_short(x):")
print(rem(z_red * k2_inverse, f, domain = 'GF(2)'))
print(y_short)

print("---------------")
print("Check k2_inv \circ M_{z_red} = y:")
#z_red_arr =[0,0,1,0]
z_red_mat = matrix_rep(z_red_arr)
#b_red_mat = matrix_rep(b_red_arr)
print("M_z' = ", matrix_rep(z_red_arr))
print("C_b =",  b_matrix)
k2z = np.dot(k2_inverse_arr, z_red_mat) % 2
k1b = np.dot(k1_array, b_matrix) % 2

for a in k2z:
	a = int(a)
#for b in k1b:
#	b = int(b)

print("Matrix k2_prime * z_prime", k2z + [0,0,0,0]) 
print("Matrix k1_prime * C_b", (k1b + v_array) % 2)

print("Check original matrix k1 * b + v", y_array)

print("-----TEST RANDOM------")
testy = [1,1,1,0]
testk= [1,1,1,1,0]
print(np.dot(testy, landscape(testk, n))%2)

