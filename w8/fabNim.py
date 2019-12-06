# from math import ceil

def play(n = 100, m = 2, playerFirst = False, takeAllToWin = True):

	def pickFromState(state, pick):
		return (state[0] - pick, min(state[0] - pick, m * pick))

	def getKernel(s):
		d = kernel[s[0]]
		if s[1] == 0 and s[0]:
			raise Exception("Called getKernel with state {} out of bound.".format(s))
		if s[0] == 0:
			return -1 if takeAllToWin else 0
		if d['lower'] >= s[1]:
			return -1
		if d['upper'] <= s[1]:
			return d['steps']

		for i in range(d['lower'] + 1, s[1] + 1):
			if getKernel(pickFromState(s, i)) == -1:
				d['upper'] = i
				d['steps'] = i
				d['lower'] = i - 1
				return getKernel(s)

		d['lower'] = s[1]
		return getKernel(s)

	def findNextStep(state, get_all = False):
		if not get_all:
			for i in reversed(range(1, state[1] + 1)):
				if getKernel(pickFromState(state, i)) == -1:
						return i
			return -1
		else:
			return [i for i in range(1, state[1] + 1) if getKernel(pickFromState(state, i)) == -1]

	def parseInput(s):
		try:
			s = int(s)
			if s == 0:
				print("You have to take at least 1 piece.")
				return False
			return s
		except Exception as e:
			print("Unable to parse the input:", e)
			return False

	def state2graph(state):
		return "There are {} pieces left.".format(state[0])

	# init the kernel
	kernel = [{'upper': i + 1, 'steps': i + 1, 'lower': 0} for i in range(n + 1)]
	
	th = 0
	for i in range(n >> 9):
		percentage = i / (n >> 9) * 100
		if percentage > th:
			print("Initializing {} %".format(th))
			th += 10
		getKernel((i << 9, min(i << 9, m)))
	print("Initialization finished!")

	def getKernelGraph(stop, start = 0):
		s = "Graph of kernel:\n"
		for i in reversed(range(stop + 1)):
			for j in range(start, stop + 1):
				if i > j:
					s += " "
				elif i == 0 and j != 0:
					s += "-"
				elif getKernel((j, i)) == -1:
					s += "|"
				else:
					s += "O"
			s += "\n"
		s += ''.join([str(i % 10) for i in range(start, stop + 1)]) + "\n"
		s += ''.join(["^" if (kernel[i]['upper'] == i) else " " for i in range(start, stop + 1)])
		return s

	# test function is under develope
	def test():
		walls = [i for i in range(n) if kernel[i]['upper'] == i]
		wall_diff = [0] + [walls[i + 1] - walls[i] for i in range(len(walls) - 1)]
		l = [1]
		index = 0
		while len(l) < len(walls):
			if l[index] >= l[-1] / m:
				l.append(l[-1] + l[index])
			else:
				index += 1

		for i in range(len(walls)):
			if walls[i] != l[i]:
				for i in range(walls):
					print(walls[i], l[i])
				raise Exception("Wrong guess!")
		print("Finish testing for n = {}, m = {}".format(n, m))
		return walls, l

	# print(test())

	def get_ans():
		if takeAllToWin:
			state = (n, n - 1)
		else:
			state = (n, n - 2)

		print("All must-win move:", findNextStep(state, get_all = True))

	def startGame():
		# setup the game conditions
		if takeAllToWin:
			state = (n, n - 1)
			print("Take all to win!\n")
		else:
			state = (n, n - 2)
			print("Take all will lose!\n")

		if playerFirst:
			turn = 0
		else:
			turn = 1

		while True:
			
			print(state2graph(state))
			
			if state == (0, 0):
				print("GG")
				break

			if turn == 0:
				userInput = parseInput(input("Your pick({} at most):".format(state[1])))
				if not userInput:
					continue
				else:
					move = userInput

			if turn == 1:
				next_pick = findNextStep(state)

				if next_pick == -1:
					print("I surrender.")
					break
				else:
					print("My pick {}.\n".format(next_pick))
					move = next_pick

			if move > state[1]:
				print("You can only take {} pieces at most.".format(state[1]))
				continue
				
			state = pickFromState(state, move)
			turn = (turn + 1) % 2

	print(getKernelGraph(30, start = 0))
	get_ans()
	
	w, l = test()

	for i in range(len(w)):
		print(i, w[i], w[i+1] - w[i])

	startGame()

# play(n = 100000, m = 2, takeAllToWin = True, playerFirst = True)
# play(n = 100000, m = 2, takeAllToWin = False, playerFirst = False)
play(n = 30, m = 3, takeAllToWin = True, playerFirst = True)
# play(n = 30, m = 3, takeAllToWin = False, playerFirst = False)
