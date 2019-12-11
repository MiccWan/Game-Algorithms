def play(n = 3, playerFirst = True):

	availableMoves = tuple((i, j) for j in range(n) for i in range(n))
	print(availableMoves)

	def moveFromState(state, move, turn):
		newState = [line.copy() for line in state]
		newState[move[0]][move[1]] = turn
		return newState
	
	def isAvailableMove(state, move):
		return state[move[0]][move[1]] == 0

	# eval a state for a specific player with MinMax
	def evalAState(state, player, layer = 0):
		over = isOver(state)
		if over == 1 or over == -1:
			return over
		if over == "Draw":
			return 0
		if layer > 15:
			print("WTF")
		if layer % 2 == 0:
			res = max([evalAState(moveFromState(state, move, player), player, layer + 1) for move in availableMoves if isAvailableMove(state, move)])
			# if layer == 2:
				# print("Evaling state\n{}".format(state2graph(state)))
				# print("Result:", res)
			return res
		else:
			return min([evalAState(moveFromState(state, move, -player), player, layer + 1) for move in availableMoves if isAvailableMove(state, move)])

	def findNextStep(state, turn):
		best_val = 1
		best_move = 0
		for move in availableMoves:
			if isAvailableMove(state, move):
				print("Tring {}".format(move))
				new_val = evalAState(moveFromState(state, move, turn), -turn)
				print("If do {}, val = {}".format(move, new_val))
				if new_val < best_val:
					best_val = new_val
					best_move = move
		return best_move if best_move else -1

	def state2graph(state):
		graph = [" " + " | ".join(map(lambda x: " OX"[x], line)) + " " for line in state]
		graph = ("\n" + "-" * (n*4-1) + "\n").join(graph)
		return graph

	def isOver(state):
		for i in range(n):
			s = sum(state[i])
			if s == n:
				return 1
			if s == -n:
				return -1
			s = sum([state[j][i] for j in range(n)])
			if s == n:
				return 1
			if s == -n:
				return -1
		s = sum((state[i][i] for i in range(n)))
		if s == n:
			return 1
		if s == -n:
			return -1
		s = sum((state[i][n - i - 1] for i in range(n)))
		if s == n:
			return 1
		if s == -n:
			return -1
		if sum([sum([abs(i) for i in line]) for line in state]) == n * n:
			return "Draw"
		return 0

	def parseInput(s):
		try:
			s = s.split(" ")
			s = filter(lambda x: x != "", s)
			s = tuple(map(int, s))
			if len(s) != 2:
				print("You have to input 2 integers. e.g. \"0, 2\"")
				return False
			if max(s) > n - 1 or min(s) < 0:
				print("Position is between [0, {}]".format(n-1))
			return s
		except Exception as e:
			print("Unable to parse the input:", e)
			return False

	def startGame():

		# init the state
		state = [[0] * n for i in range(n)]

		if playerFirst:
			turn = 1
		else:
			turn = -1

		while True:
			
			print(state2graph(state))
			
			print(isOver(state))
			if isOver(state):
				print("GG")
				break

			if turn == 1:
				userInput = parseInput(input("(x, y) = ?"))
				if not userInput:
					continue
				else:
					move = userInput

			if turn == -1:
				print("Calling findNextStep function.")
				next_move = findNextStep(state, turn)

				if next_move == -1:
					print("I surrender.")
					break
				else:
					print("I'll do {}.\n".format(next_move))
					move = next_move

			if not isAvailableMove(state, move):
				print("Invalid move!")
				continue
				
			state = moveFromState(state, move, turn)
			turn = -turn

	startGame()

play(n = 4)