def play(n = 3, piece_max = 3, piece_num = 2, playerFirst = True, printAfter = 10):

    N = n * n
    positions = list(range(N))
    pieces = list(range(1, piece_max + 1)) + list(range(-1, -piece_max - 1, -1))
    print("pieces =", pieces)

    def getAvailableMoves(state, left, onlyPos = False):
        # print("Finding valid moves for state = {}, left = {}".format(state, left))
        for piece in pieces:
            if not left[piece]:
                continue
            if onlyPos and piece < 0:
                continue
            if not onlyPos and piece > 0:
                continue
            else:
                for pos in positions:
                    if abs(state[pos]) < abs(piece):
                        yield (piece, pos)

    def getChildNodes(state, left):
        for piece, pos in getAvailableMoves(state, left):
            yield moveFromState(state, left, piece, pos)

    # for piece, pos in getAvailableMoves([3, 3, -3, 3, 3, -3, 2, 1, -1], [0,1,2,2,0,1,1]):
    #     print(piece, pos)

    def isAvailableMove(state, left, piece, pos):
        if not left[piece]:
            print("No any {} left. left = {}".format(piece, left))
            return False
        if abs(state[pos]) >= abs(piece):
            print("The piece in {} is {}, not smaller than your move {}".format(pos, state[pos], piece))
            return False
        return True

    def moveFromState(state, left, piece, pos):
        if not isAvailableMove(state, left, piece, pos):
            return
        new_state = state.copy()
        new_state[pos] = piece
        new_left = left.copy()
        new_left[piece] -= 1
        return new_state, new_left

    def hasWinner(state):
        def zip2One(x):
            if x:
                return int(x/abs(x))
            else:
                return x
        # print("Converting state...")
        # print(state)
        state = list(map(zip2One, state))
        # print(state)
        for i in range(n):
            s = sum([state[i*n + j] for j in range(n)])
            if s == n:
                return 1
            if s == -n:
                return -1
            s = sum([state[i + j*n] for j in range(n)])
            if s == n:
                return 1
            if s == -n:
                return -1
        s = sum((state[i*n + i] for i in range(n)))
        if s == n:
            return 1
        if s == -n:
            return -1
        s = sum((state[i* n + (n - i - 1)] for i in range(n)))
        if s == n:
            return 1
        if s == -n:
            return -1
        return 0

    def abminmax(state, left, depth = piece_max * piece_num * 2 + 1, alpha = -1, beta = 1, maximizing = False):
        if depth == 0:
            raise Exception("Depth 0!")
            return (0,)
        winner = hasWinner(state)
        if winner:
            # print("Found winner! Returning", winner)
            return (winner,)
        if sum(left) == 0:
            # print("No pieces left, returning 0")
            return (0,)
        if maximizing:
            # print("Find Maximum move in")
            # print("state =", state)
            # print("left =", left)
            # print("availableMoves =", list(getAvailableMoves(state, left, onlyPos = True)))
            value = -2
            best_piece = 0
            best_pos = -1
            for piece, pos in getAvailableMoves(state, left, onlyPos = True):
                # print("Going {} at {}.".format(piece, pos))
                child_node = abminmax(*moveFromState(state, left, piece, pos), depth - 1, alpha, beta, False)
                # print("child_node =", child_node)
                if child_node[0] > value:
                    best_piece, best_pos = piece, pos
                    value = child_node[0]
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        # print("Alpha pruning on depth {}".format(depth))
                        # print("state =", state)
                        # print("result =", value, best_piece, best_pos)
                        # print("alpha, beta", alpha, beta)
                        break
            # print("now is Maximizing")
            # print("Returning", value, best_piece, best_pos)
            if depth > printAfter:
                print(depth)
                print(value, best_piece, best_pos)
            return (value, best_piece, best_pos)
        else:
            # print("Find minimum move in")
            # print("state =", state)
            # print("left =", left)
            # print("availableMoves =", list(getAvailableMoves(state, left, onlyPos = False)))
            value = 2
            best_piece = 0
            best_pos = -1
            for piece, pos in getAvailableMoves(state, left, onlyPos = False):
                # print("Going {} at {}.".format(piece, pos))
                child_node = abminmax(*moveFromState(state, left, piece, pos), depth - 1, alpha, beta, True)
                # print("child_node =", child_node)
                if child_node[0] < value:
                    best_piece, best_pos = piece, pos
                    value = child_node[0]
                    beta = min(beta, value)
                    if alpha >= beta:
                        # print("Beta pruning on depth {}".format(depth))
                        # print("state =", state)
                        # print("result =", value, best_piece, best_pos)
                        # print("alpha, beta", alpha, beta)
                        break
            # print("now is minimizing")
            # print("Returning", value, best_piece, best_pos)
            if depth > printAfter:
                print(depth)
                print(value, best_piece, best_pos)
            return (value, best_piece, best_pos)

    def findNextStep(state, left):
        search_result = abminmax(state, left)
        return search_result

    def state2graph(state):
        print("Drawing", state)
        graph = [state[i*n:i*n+n] for i in range(n)]
        graph = ["|".join(map(lambda x: (" " if x >= 0 else "") + str(x) + " ", line)) for line in graph]
        graph = ("\n" + "-" * (n*4-1) + "\n").join(graph)
        return graph

    # print(state2graph([0,0,0,1,2,-3,-3,-3,-3]))

    def parseInput(s):
        try:
            s = s.split(" ")
            s = filter(lambda x: x != "", s)
            s = tuple(map(int, s))
            if len(s) != 2:
                print("You have to input 2 integers. e.g. \"0, 2\"")
                return False
            if s[1] < 0 or s[1] > N - 1:
                print("Position must between [0, {}]".format(N-1))
                return False
            return s
        except Exception as e:
            print("Unable to parse the input:", e)
            return False

    def startGame():

        # init the state
        state = [0] * N
        left = [0] + ([piece_num] * piece_max * 2)

        turn = 1 if playerFirst else -1

        while True:
            
            print("New loop")
            print(state2graph(state))
            
            # print("hasWinner(state) =", hasWinner(state))
            if hasWinner(state):
                print("GG")
                break
            if sum(left) == 0:
                print("Draw!")
                break

            if turn == 1:
                userInput = parseInput(input("(piece, pos) = ?"))
                if not userInput:
                    continue
                else:
                    piece, pos = userInput

            if turn == -1:
                print("Calling findNextStep function.")
                value, best_piece, best_pos = findNextStep(state, left)
                print("Searching result =", value, best_piece, best_pos)

                if value == 1:
                    print("I surrender.")
                    break
                else:
                    print("I'll go {} at {}.\n".format(best_piece, best_pos))
                    piece, pos = best_piece, best_pos

            if not isAvailableMove(state, left, piece, pos):
                print("Invalid move!")
                continue
                
            state, left = moveFromState(state, left, piece, pos)
            turn = -turn

    startGame()

play(playerFirst=True)