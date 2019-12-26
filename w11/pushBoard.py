import math

def pushBoard(n = 3, maxDepth = math.inf):

    N = n*n

    class Board:
        def __init__(self, l = list(range(N))):
            if len(l) != N:
                raise Exception("The object creating a Board must be length {}, but get {}.".format(N, len(l)))
            self.state = [e for e in l]

        def get(self):
            return tuple(self.state)

        def push(self, i, j):
            l = self.state.copy()
            l[i], l[j] = l[j], l[i]
            return Board(l)

        def childNodes(self):
            for index in range(N):
                if self.state[index] == N - 1:
                    i = index // n
                    j = index % n
                    if i - 1 >= 0: yield self.push(i * n + j, (i - 1) * n + j)
                    if i + 1 < n: yield self.push(i * n + j, (i + 1) * n + j)
                    if j - 1 >= 0: yield self.push(i * n + j, i * n + (j - 1))
                    if j + 1 < n: yield self.push(i * n + j, i * n + (j + 1))
                    break


    def BFS(maxDepth = maxDepth):

        state = Board()
        stateQueue = [(state.get(), 0, 0)]
        history = set([state.get()])
        i = 0

        while i < len(stateQueue):
            if not i % 100000:
                print(i)
            if stateQueue[i][2] > maxDepth:
                break
            for childState in Board(stateQueue[i][0]).childNodes():
                if childState.get() in history: continue
                stateQueue.append((childState.get(), i, stateQueue[i][2] + 1))
                history.add(childState.get())
            i += 1

        count = [0] * (stateQueue[-1][2] + 1)

        for i in range(len(stateQueue)):
            count[stateQueue[i][2]] += 1

        for i in range(len(count)):
            print("With {} step, we can reach {} different board.".format(i, count[i]))

        return count

    return BFS()

pushBoard(4)