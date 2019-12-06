ans_cnt = 0

def applyRepSelections(data, m, callback):
    
    n = len(data)
    l = [0] * m
    
    while True:

        callback([data[i] for i in l])
        f_found = False
        
        for i in reversed(range(m)):
            if l[i] < n - 1:
                f_found = True
                break

        if not f_found:
            return

        l[i] = l[i] + 1
        for j in range(i+1, m):
            l[j] = l[i]

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
    def useDecSwapAlg(slm):
        if (slm[0] * 1000 + slm[1] * 100 + slm[2] * 10 + slm[3]) == 4 * (slm[3] * 1000 + slm[2] * 100 + slm[1] * 10 + slm[0]):
            print(slm)
            global ans_cnt
            ans_cnt = ans_cnt + 1
    decSwapAlg(lm, len(lm), useDecSwapAlg)


d = list(range(10))

applyRepSelections(d, 4, useSelections)

print("ans_cnt = {}".format(ans_cnt))

