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

d = list(range(1, 10))

def useSelections(lm):
    if sum(lm) == 20:
        global ans_cnt
        ans_cnt = ans_cnt + 1
        print(lm)

for i in range(21):
    applyRepSelections(d, i, useSelections)

print(ans_cnt)