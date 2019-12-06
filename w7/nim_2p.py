def getAvailables(n, most_take=3):
	availables = []

	for take in range(1, most_take + 1):
		# print("Finding take =", take)
		
		## up to down + left-up to right-down
		for i in range(n + 1 - take):
			for j in range(i + 1):
				# print("Finding ud, lurd and lr for (i, j) = ({}, {})".format(i, j))
				ud, lurd, lr = 0, 0, 0
				botton_pos = ((i+take-1)*(i+take) >> 1) + j
				for k in range(take):
					layer_k_pos = ((i+k)*(i+k+1) >> 1) + j
					ud |= 1 << (layer_k_pos)
					lurd |= 1 << (layer_k_pos + k)
					lr |= 1 << (botton_pos + k)

				# print("Appended", ud, lurd)
				availables.append(ud)
				if take != 1:
					availables.append(lurd)
					availables.append(lr)

	return availables

# print(len(getAvailables(5, most_take = 5)))


# =================
#  take all to win
# =================

def play(n = 5, most_take = 3, playerFirst = True):

	# init the availables and the kernel
	N = n*(n+1) >> 1
	availables = sorted(getAvailables(n, most_take = most_take))
	kernel = [-1] * (1 << N)
	for i in availables: kernel[i] = i
	kernel[0] = 0

	# kernal after init
	# print(kernel[:200])

	def findNextStep(state):
		if kernel[state] >= 0:
			return kernel[state]
		for pick in availables:
			# check the pick is valid
			if ~state & pick == 0:
				# recursive to next state
				if findNextStep(state^pick) == 0:
					kernel[state] = pick
					return kernel[state]
		
		kernel[state] = 0
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
		s = ""
		cnt = 0
		for i in range(n):
			s += "  " * (n - i)
			for j in range(i + 1):
				if state & (1 << cnt):
					s += '%02d' % cnt
				else:
					s += "~~"
				s += "  "
				cnt += 1
			s += "\n"

		return s

	def state2str(num):
		# print("in state2str num =",num)
		return " ".join([str(i) for i in range(N) if (num & (1 << i))])

	# game part
	state = len(kernel) - 1

	player = 0

	while True:
		
		print()
		print(state2graph(state))
		userInput = parseInput(input("{}P:".format(player + 1)))
		

		if not userInput:
			print("Invalid input.")
			continue
		if not userInput in availables:
			print("Invalid move.")
			continue
		if not ~state & userInput == 0:
			print("Invalid pick in this state.")
			continue

		state ^= userInput

		player = (player + 1) % 2

		if state == 0:
			print("GG")
			break
play(n = 4)