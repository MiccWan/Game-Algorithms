n = int(input("n = "))

r = list(range(1, 1+n))

def swap(l, a, b):
	l[a], l[b] = l[b], l[a]
	return l

def decSwapAlg(l, n):

	while True:

		print(l)
		for i in reversed(range(n)):
			if i == 0:
				return
			if l[i-1] < l[i]:
				i = i - 1
				break

		for j in range(i+1, n):
			if l[j] < l[i]:
				j = j - 1
				break

		l = swap(l, i, j)

		l[i+1:] = l[i+1:][::-1]

decSwapAlg(r, n)
