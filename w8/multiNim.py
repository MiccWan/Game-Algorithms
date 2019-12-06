def play(originState = (5,4,3), mostTake = 0, playerFirst = False, takeAllToWin = True):

	def pickFromState(state, pick):
		# print(state, "-", pick, "=", tuple((state[i] if i != pick[0] else state[i] - pick[1]) for i in range(n)))
		return tuple((state[i] if i != pick[0] else state[i] - pick[1]) for i in range(n))

	def isOverTake(state, pick):
		for i in pickFromState(state, pick):
			if i < 0: 
				return True
		return False

	def getKernel(state):
		if kernel.get(state) == None:
			for i in range(n):
				for j in range(1, (min(state[i], mostTake) if mostTake else state[i]) + 1):
					if getKernel(pickFromState(state, (i, j))) == -1:
						kernel[state] = (i, j)
						return kernel[state]
			kernel[state] = -1
		return kernel[state]

	def parseInput(s):
		try:
			s = s.split(" ")
			s = filter(lambda x: x!="", s)
			s = tuple(map(int, s))
			if len(s) != 2:
				print("Input should be two integers.")
				return False
			if s[0] >= n:
				print("Picking index out of range.")
				return False
			if isOverTake(state, s):
				print("Invalid move in this state.")
				return False
			if mostTake > 0:
				if s[1] > mostTake:
					print("You can only take {} pieces at most.".format(mostTake))
					return False
			return s
		except:
			print("Unable to parse the input.")
			return False

	def state2graph(state):
		s = str(state) + "\n"
		for i in state:
			s += "%02d" % i + " | " + "O" * i + "\n"
		return s

	# game part
	state = originState

	# init the availables and the kernel
	n = len(originState)
	kernel = dict()

	# setup the game conditions
	if takeAllToWin:
		kernel[(0,) * n] = -1
		print("Take all to win!\n")
	else:
		kernel[(0,) * n] = (0, 0)
		print("Take all will lose!\n")

	if playerFirst:
		turn = 0
	else:
		turn = 1

	while True:
		
		print(state2graph(state))
		
		if turn == 0:
			userInput = parseInput(input("Your pick:"))
			if not userInput:
				continue
			else:
				move = userInput

		if turn == 1:
			next_pick = getKernel(state)
			if next_pick == -1:
				print("I surrender.")
				break
			else:
				print("My pick {}.\n".format(str(next_pick)))
				move = next_pick
			# print(kernel)
			
		state = pickFromState(state, move)
		turn = (turn + 1) % 2
		if state == (0,) * n:
			print("GG")
			break

play(originState = (9, 8, 7), mostTake = 3, takeAllToWin = True, playerFirst = True)