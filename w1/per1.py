def swap(l, a, b):
	l[a], l[b] = l[b], l[a]
	return l

def permutation1(a, m):
	if m == 1:
		print(a)
		return
	for i in range(m):
		a = swap(a, i, m-1)
		permutation1(a, m-1)
		a = swap(a, i, m-1)
 
n = int(input("n = "))

l = list(range(1, 1+n))

permutation1(l, len(l))