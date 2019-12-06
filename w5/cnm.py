def applySelections(data, m, callback):
    
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

n = 9
m = 4
d = list(range(1, n+1))

applySelections(d, m, print)

