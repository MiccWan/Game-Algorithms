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

n = 9
m = 4
d = list(range(1, n+1))

def useSelections(lm):
    if sum(lm) == 20:
        global ans_cnt
        ans_cnt = ans_cnt + 1
        print(lm)

applyRepSelections(d, m, useSelections)

print("Answer count: {}".format(ans_cnt))