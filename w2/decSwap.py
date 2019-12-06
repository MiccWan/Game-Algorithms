# must set list l manually
l = [5, 1, 1, 2, 2]

ans_cnt = 0

def test(l):
	global ans_cnt
	ans_cnt = ans_cnt + 1
	print(ans_cnt, " -> ", l)

def swap(l, a, b):
	l[a], l[b] = l[b], l[a]
	return l

def decSwapAlg(l, n, callback):

	while True:

		callback(l.copy())

		for i in reversed(range(n)):
			if i == 0:
				return
			if l[i-1] < l[i]:
				i = i - 1
				break

		for j in range(i+1, n):
			if l[j] <= l[i]:
				j = j - 1
				break

		l = swap(l, i, j)

		l[i+1:] = l[i+1:][::-1]

l.sort()
decSwapAlg(l, len(l), test)
