def getAvailables(n, most_take=3):
	availables = []

	for take in range(1, most_take + 1):
		
		## ud = up to down
		## lurd = left-up to right-down
		## lr = left to right
		for i in range(n + 1 - take):
			for j in range(i + 1):
				ud, lr, lurd = 0, 0, 0
				botton_pos = ((i+take-1)*(i+take) >> 1) + j
				for k in range(take):
					layer_k_pos = ((i+k)*(i+k+1) >> 1) + j
					ud |= 1 << (layer_k_pos)
					lr |= 1 << (botton_pos + k)
					lurd |= 1 << (layer_k_pos + k)

				availables.append(ud)
				availables.append(lr)
				availables.append(lurd)

	return sorted(availables)

def play(n = 5, most_take = 3, playerFirst = False, takeAllToWin = True):

	# init the availables and the kernel
	N = (n*(n+1) >> 1 )
	availables = getAvailables(n, most_take = most_take)
	kernel = [-2] * (1 << N)

	# set the final state of kernel
	if takeAllToWin:
		kernel[0] = -1
	else:
		kernel[0] = 0

	def findNextStep(state):
		if kernel[state] == -2:
			for move in availables:
				# check the pick is valid
				if ~state & move == 0:
					# recursive to next state
					if findNextStep(state^move) == -1:
						kernel[state] = move
						return kernel[state]
			
			kernel[state] = -1
		return kernel[state]

	def parseInput(s):
		try:
			s = s.split(" ")
			s = filter(lambda x: x!="", s)
			l = list(map(lambda x: 1 << int(x), s))
			return sum(l)
		except:
			return False

	def state2graph(state):
		pattern = [list(range((i*(i+1)>>1), ((i*(i+1)>>1) + i + 1))) for i in range(n)]

		width = (max([len(l) for l in pattern]) * 2 - 1) * 2

		graph = ""
		for l in pattern:
			l_graph = "  ".join([(('%02d' % i) if (state & (1 << i)) else "~~") for i in l ])
			padding = " " * ((width - len(l_graph)) >> 1)
			graph += padding + l_graph + padding + "\n"

		return graph

	def num2ans(num):
		return "02356789ab14c"[num]

	def state2str(num):
		return ", ".join([str(i) for i in range(N) if (num & (1 << i))])

	# print some information for hw
	ori_state = (1 << N) - 1
	print("=================================")
	print("There are {} moves are available.".format(len(availables)))
	print("The following are must-win moves:")
	for move in availables:
		if findNextStep(ori_state ^ move) == -1:
			print(state2str(move))
	print("=================================\n")

	# game part
	state = len(kernel) - 1

	if takeAllToWin:
		print("Take all to win!\n")
	else:
		print("Take all will lose!\n")

	turn = 0 if playerFirst else 1
	while True:
		
		print(state2graph(state))
		
		if turn == 0:
			userInput = parseInput(input("Your pick:"))
			if not userInput:
				print("Invalid input.")
				continue
			if not userInput in availables:
				print("Invalid move.")
				continue
			if not ~state & userInput == 0:
				print("Invalid move in this state.")
				continue
			move = userInput

		if turn == 1:
			next_pick = findNextStep(state)
			if next_pick == -1:
				print("I surrender.")
				break
			else:
				if not ~state & next_pick == 0:
					print("Computer made an invalid move!?")
					raise Exception("Bad AI.")
				print("My pick [{}].\n".format(state2str(next_pick)))
				move = next_pick
			
		state ^= move
		turn = (turn + 1) % 2
		if state == 0:
			print("GG")
			break

play(n = 4, most_take = 3, takeAllToWin = True, playerFirst = True)