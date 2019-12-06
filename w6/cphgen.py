def handleInput(data):
    if isinstance(data, int):
        n = data
        data = list(range(n))
    elif isinstance(data, str):
        n = len(data)
    elif isinstance(data, list):
        n = len(data)
    else:
        raise Exception("Unsupported data type {}".format(type(data)))
    return data, n

def cnm(data, m):
    
    data, n = handleInput(data)

    def rec(selected, index):
        if len(selected) == m:
            yield [data[i] for i in selected]
            return
        if index == len(data):
            return
        yield from rec(selected + [index], index+1)
        yield from rec(selected, index+1)

    yield from rec([], 0)

def pnm(data, m):

    data, n = handleInput(data)

    for comb in cnm(sorted(data), m):
        yield from decSwap(comb)

    # rearrange combination from cnm
    def decSwap(l):

        while True:

            yield [data[i] for i in l]

            # keep generate next permutation
            for i in reversed(range(m)):
                if i == 0:
                    return
                if l[i-1] < l[i]:
                    i = i - 1
                    break

            for j in range(i+1, m):
                if l[j] <= l[i]:
                    j = j - 1
                    break

            l[i], l[j] = l[j], l[i]

            l[i+1:] = l[i+1:][::-1]

    applySelections()

for i in cnm([0,0,1,1],2):
    print(i)

# papply(7, 4, print)
# papply([7,6,5,4,3,2], 4, print)
# papply([7,6,5,4,3,2], 4, print, sort = False)
# papply("7654321", 4, print)