def applySubSelections(data, callback, m="all"):

    def applyMSelections(data, m, callback):
        n = len(data)
        l = list(range(m))
        
        while True:

            callback([data[i] for i in l])
            f_found = False
            
            for i in reversed(range(m)):
                if l[i] < n - m + i:
                    f_found = True
                    break

            if not f_found:
                return

            l[i] = l[i] + 1
            for j in range(i+1, m):
                l[j] = l[i] + j - i

    if m == "all":
        for i in range(len(data)+1):
            applyMSelections(data, i, callback)
        return

    if isinstance(m, int):
        if m > len(data):
            raise Exception("Can't choose {} elements from length {} data.".format(m, len(data)))
        else:
            applyMSelections(data, m, callback)
    else:
        raise Exception("m must be an integer or a string \"all\", but get {}.".format(m))
n = 5
d = list(range(1, n+1))

applySubSelections(d, print)

