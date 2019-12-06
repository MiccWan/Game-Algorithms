ans_cnt = 0

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

m = 4
d = list(range(1, 10))

def useSelections(lm):
    if sum(lm) == 20:
        print(lm)
        global ans_cnt
        ans_cnt = ans_cnt + 1

applySelections(d, m, useSelections)

print("Answer count: {}".format(ans_cnt))