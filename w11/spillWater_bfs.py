import math

def spillWater(cups = [3, 5], target = 4, printAns = False, maxDepth = math.inf, runAll = False):

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

    def BFS(maxDepth = maxDepth):
        state = State()
        stateQueue = [(state.get(), 0, 0)]
        history = set([state.get()])
        i = 0
        ans = []

        while i < len(stateQueue):
            if stateQueue[i][2] > maxDepth:
                break
            if target in stateQueue[i][0]:
                while len(ans) <= stateQueue[i][2]:
                    ans.append(0)
                ans[stateQueue[i][2]] += 1
                if not runAll:
                    maxDepth = min(maxDepth, stateQueue[i][2])
                if printAns:
                    trace = i
                    path = [stateQueue[trace][0]]
                    while trace != 0:
                        trace = stateQueue[trace][1]
                        path.append(stateQueue[trace][0])
                    print(stateQueue[i][2], list(reversed(path)))
            elif not stateQueue[i][2] == maxDepth:
                for newState in State(list(stateQueue[i][0])).childNodes():
                    if newState.get() in history:
                        continue
                    stateQueue.append((newState.get(), i, stateQueue[i][2] + 1))
                    history.add(newState.get())
            i += 1

        for step, num in enumerate(ans):
            print("Step {} has {} way(s) to get 7.".format(step, num))

        return ans

    return BFS()

spillWater([18, 19, 20, 21], target = 7, printAns = False, runAll = True)