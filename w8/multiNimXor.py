from functools import reduce

def play(originState = (5,4,3), mostTake = 0, playerFirst = False, takeAllToWin = True):

	def pickFromState(state, pick):
		# print(state, "-", pick, "=", tuple((state[i] if i != pick[0] else state[i] - pick[1]) for i in range(n)))
		return tuple((state[i] if i != pick[0] else state[i] - pick[1]) for i in range(n))

	def isOverTake(state, pick):
		for i in pickFromState(state, pick):
			if i < 0: 
				return True
		return False

	def findNextStep(state):
		# pick = max -  red ^ max
		pick_index = state.index(max(state))
		pick_num = max(state) - (reduce(lambda x, y: x^y, state) ^ max(state))
		if pick_num:
			return (pick_index, pick_num)
		else:
			return -1

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
		except Exception as e:
			print("Unable to parse the input:", e)
			return False

	def state2graph(state):
		s = str(state) + "\n"
		for i in state:
			s += "%02d" % i + " | " + "O" * i + "\n"
		return s

	# game part
	state = originState
	n = len(originState)

	# setup the game conditions
	if takeAllToWin:
		print("Take all to win!\n")
	else:
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
			next_pick = findNextStep(state)
			if next_pick == -1:
				print("I surrender.")
				break
			else:
				print("My pick {}.\n".format(str(next_pick)))
				move = next_pick
			
		state = pickFromState(state, move)
		turn = (turn + 1) % 2
		if state == (0,) * n:
			print("GG")
			break

play(originState = (9, 8, 7), mostTake = 0, takeAllToWin = True, playerFirst = True)
