from math import comb, log2

m = 269
n = m - 1
q = 8
code_length = q*n
i = 1
sum = 1
while log2(sum) < code_length - (2*m - 1):
	sum += comb(code_length, i)
	i += 1
print(i)
print("code_length:", code_length)
print("code_dimens:", (2*m - 1))
