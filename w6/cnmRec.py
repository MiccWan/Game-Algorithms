def applyRecSelections(data, m, callback):
    data = list(range(data))
    # data.sort()

    def rec(data, selected, n, m, callback):
        if len(selected) == m:
            callback([data[i] for i in selected])
            return
        if n == len(data):
            return
        rec(data, selected + [n], n+1, m, callback)
        rec(data, selected, n+1, m, callback)

    rec(data, [], 0, m, callback)

# applyRecSelections(list(range(1, 10)), 4, print)

