def play(available = [1, 3, 4], target = [7,11,13,17], playerFirst = True):

	# variable setup
	MAX = max(target)
	
	# build kernel
	kernel = [(0 if i in target else -1) for i in range(MAX + 1)]
	for i in reversed(range(MAX)):
		if not kernel[i] < 0: continue
		for j in available:
			if i + j < MAX + 1:
				if kernel[i + j] == 0:
					kernel[i] = i + j
					break
		if kernel[i] < 0: kernel[i] = 0

	# print to check the kernel
	for key,val in enumerate(kernel):
		print(key, val)
	
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
		if kernel[userInput] == 0:
			print("I surrender.")
			break
		else:
			now = kernel[userInput]
			if now in target:
				print("{} GG".format(now))
				break

play()