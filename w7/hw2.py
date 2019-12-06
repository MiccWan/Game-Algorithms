def getAvailables(n, most_take=3):
	availables = []

	for take in range(1, most_take + 1):
		# print("Finding take =", take)
		
		## ud = up to down
		## lurd = left-up to right-down
		## lr = left to right
		for i in range(n + 1 - take):
			for j in range(i + 1):
				ud, lurd, lr = 0, 0, 0
				botton_pos = ((i+take-1)*(i+take) >> 1) + j
				for k in range(take):
					layer_k_pos = ((i+k)*(i+k+1) >> 1) + j
					ud |= 1 << (layer_k_pos)
					lurd |= 1 << (layer_k_pos + k)
					lr |= 1 << (botton_pos + k)

				availables.append(ud)
				if take != 1:
					availables.append(lurd)
					availables.append(lr)

		def state2num(l):
			num = 0
			for i in l:
				num ^= 1 << i
			return num
		
		## the three additional pieces
		additional = []
		lines = [[10, 1, 2, 11], [10, 3, 7, 12], [11, 5, 8, 12]]

		for line in lines:
			for i in range(1, most_take + 1):
				additional.append(state2num(line[:i]))
				additional.append(state2num(line[i:]))

	return sorted(availables + list(filter(lambda x: x != 0, set(additional))))

def play(n = 5, most_take = 3, playerFirst = False):

	# init the availables and the kernel
	N = (n*(n+1) >> 1 ) + 3
	availables = getAvailables(n, most_take = most_take)
	kernel = [-2] * (1 << N)
	print(len(kernel))

	# =================
	#  take all to win
	# =================
	# kernel[0] = -1

	# =================
	#  take all will lose
	# =================
	kernel[0] = 0

	def findNextStep(state):
		if kernel[state] != -2:
			return kernel[state]
		for pick in availables:
			# check the pick is valid
			if ~state & pick == 0:
				# recursive to next state
				if findNextStep(state^pick) == -1:
					kernel[state] = pick
					return pick
		
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
		pattern = [[0], [10, 1, 2, 11], [3, 4, 5], [6, 7, 8, 9], [12]]

		width = (max([len(l) for l in pattern]) * 2 - 1) * 2

		graph = ""
		for l in pattern:
			l_graph = "  ".join([(('%02d' % i) if (state & (1 << i)) else "~~") for i in l ])
			padding = " " * ((width - len(l_graph)) >> 1)
			graph += padding + l_graph + padding + "\n"

		return graph

	def state2str(num):
		# print("in state2str num =",num)
		return " ".join([str(i) for i in range(N) if (num & (1 << i))])

	ori_state = (1 << N) - 1
	print("There are {} moves are available.".format(len(availables)))
	print("The following are must-win moves:")
	for move in availables:
		# print(state2str(move))
		if findNextStep(ori_state ^ move) == -1:
			print(state2str(move))

	# game part
	state = len(kernel) - 1

	while True:
		if not playerFirst:
			playerFirst = True
			userInput = 0
		else:
			print(state2graph(state))
			userInput = parseInput(input("Your pick:"))
			print()
			if not userInput:
				print("Invalid input.")
				continue
			if not userInput in availables:
				print("Invalid move.")
				continue
			if not ~state & userInput == 0:
				print("Invalid pick in this state.")

		state ^= userInput
		print(state2graph(state))

		next_pick = findNextStep(state)


		if next_pick == -1:
			print("I surrender.")
			break
		else:
			print("My pick {}.\n".format(state2str(next_pick)))
			state ^= next_pick
			if state == 0:
				print("GG")
				break
play(n = 4, most_take = 4)