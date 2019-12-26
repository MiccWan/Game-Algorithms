import math

def spillWater(cups = [3, 5], target = 4):

    n = len(cups)
    fullCup = cups.copy()

    class State:
        def __init__(self, l = [0] * n):
            self.state = l.copy()
        
        def fill(self, i):
            new_state = self.state.copy()
            new_state[i] = fullCup[i]
            return State(new_state)

        def drain(self, i):
            new_state = self.state.copy()
            new_state[i] = 0
            return State(new_state)

        def transfer(self, i, j):
            new_state = self.state.copy()
            capacity = fullCup[j] - new_state[j]
            transferAmount = min(capacity, new_state[i])
            new_state[i] -= transferAmount
            new_state[j] += transferAmount
            return State(new_state)

        def get(self):
            return tuple(self.state)

        def childNodes(self):
            # fill
            for i in range(n):
                yield self.fill(i)
            
            # drain
            for i in range(n):
                yield self.drain(i)
            
            # transfer
            for i in range(n):
                for j in range(n):
                    if i != j:
                        yield self.transfer(i, j)

    def BFS():
        state = State()
        stateQueue = [(state.get(), 0, 0)]
        history = set([state.get()])
        i = 0
        minDepth = math.inf
        ans = 0

        while i < len(stateQueue):
            # if stateQueue[i][2] + 1 >  minDepth:
            #     break
            if i % 10000 == 0:
                print(i)
            if target in stateQueue[i][0]:
                ans += 1
                # trace = i
                # path = [stateQueue[trace][0]]
                # while trace != 0:
                #     trace = stateQueue[trace][1]
                #     path.append(stateQueue[trace][0])
                # print(list(reversed(path)))
            else:
                for newState in State(list(stateQueue[i][0])).childNodes():
                    if not (newState.get() in history):
                        stateQueue.append((newState.get(), i, stateQueue[i][2] + 1))
                        history.add(newState.get())
                        if target in newState.get():
                            minDepth = min(minDepth, stateQueue[i][2] + 1)
            i += 1

        print(ans)
        return minDepth

    return BFS()

print(spillWater([19, 20, 21, 22], target = 7))