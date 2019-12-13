def fillDomino(m = 3, n = 6):

	if (m * n) % 2 != 0:
		return 0

	ans = [0]
	pieces = m*n >> 2
	state = [([False] * n) for i in range(m)]

	def recFill(filled = 0):
		if filled == pieces:
			ans[0] += 1
		else:
			for i in range(m):
				for j in range(n):
					if not state[i][j]:
						state[i][j] = True
						isIsolated = True
						if (j < n - 1) and (not state[i][j + 1]):
							isIsolated = False
							state[i][j + 1] = True
							recFill(filled + 1)
							state[i][j + 1] = False
						if (i < m - 1) and (not state[i + 1][j]):
							isIsolated = False
							state[i + 1][j] = True
							recFill(filled + 1)
							state[i + 1][j] = False
						state[i][j] = False
						if isIsolated:
							return

	recFill()
	print(ans[0])

fillDomino()