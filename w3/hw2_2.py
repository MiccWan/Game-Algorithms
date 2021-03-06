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
    def useDecSwapAlg(l):
        global ans_cnt
        abcde = l[0] * 10000 + l[1] * 1000 + l[2] * 100 + l[3] * 10 + l[4]
        a = l[0]
        e = l[4]
        if abcde * a == e * 111111:
            print("{} * {} = {}".format(abcde, a, e*111111))
            ans_cnt += 1
    decSwapAlg(lm, len(lm), useDecSwapAlg)

n = 9
m = 5
d = list(range(0, n+1))

applyRepSelections(d, m, useSelections)

print("ans_cnt = {}".format(ans_cnt))

