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

    def childNodes(state):
        # fill
        for i in range(n):
            yield state.fill(i)
        
        # drain
        for i in range(n):
            yield state.drain(i)
        
        # transfer
        for i in range(n):
            for j in range(n):
                if i != j:
                    yield state.transfer(i, j)
    

    state = State()

    def DFS(state, history = set([state.get()]), minDepth = math.inf):
        if len(history) > minDepth:
            return
        if target in state.get():
            if len(history) - 1 < minDepth:
                return ([state.get()], len(history) - 1)

        bestResult = None

        for node in childNodes(state):
            if not (node.get() in history):
                result = DFS(node, history | set([node.get()]), minDepth)
                if result and result[1] < minDepth:
                    bestResult = ([state.get()] + result[0], result[1])
                    minDepth = result[1]

        return bestResult
    
    return DFS(state)

print(spillWater([3, 5], target = 4))