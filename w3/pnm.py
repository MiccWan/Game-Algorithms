def applySelections(n, m, callback):
    
    l = list(range(m))
    
    while True:

        callback(l.copy())
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

def decSwapAlg(l, n, callback):

    while True:

        callback(l.copy())

        for i in reversed(range(n)):
            if i == 0:
                return
            if l[i-1] < l[i]:
                i = i - 1
                break

        for j in range(i+1, n):
            if l[j] <= l[i]:
                j = j - 1
                break

        l[i], l[j] = l[j], l[i]

        l[i+1:] = l[i+1:][::-1]

def useSelections(lm):
    print("=====")
    decSwapAlg(lm, len(lm), print)

n = 6
m = 4
d = list(range(1, n+1))

applySelections(n, m, useSelections)

