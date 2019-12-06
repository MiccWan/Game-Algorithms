def play(available = [31,23,20,3,1], target = [71], playerFirst = False):

	# variable setup
	MAX = max(target)

	# build kernel
	kernel = [(0 if i in target else -1) for i in range(MAX + 1)]

	def findNextStep(n):
		if kernel[n] >= 0:
			return kernel[n]
		for i in available:
			if n + i < MAX + 1:
				if findNextStep(n + i) == 0:
					kernel[n] = n + i
					break
		if kernel[n] == -1:
			kernel[n] = 0
		return kernel[n]

	# game part
	now = 0
	if playerFirst:
		print("You go first:")

	while True:
		if not playerFirst:
			playerFirst = True
			userInput = 0
		else:
			userInput = int(input("{}, your turn:".format(now)))
			if not (userInput - now) in available:
				print("Invalid move.")
				continue
			if userInput > MAX:
				print("Invalid move.")
				continue

		next = findNextStep(userInput)
		
		# # print to check the kernel
		# for key,val in enumerate(kernel):
		# 	print(key, val)

		if next == 0:
			print("I surrender.")
			break
		else:
			now = next
			if now in target:
				print("{} GG".format(now))
				break

play()