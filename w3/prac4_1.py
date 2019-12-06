ans_cnt = 0

def applyRepRecSelections(data, m, callback):
    l = list(range(len(data)))
    data.sort()

    def rec(data, selected, n, m, callback):

        if len(selected) == m:
            callback([data[i] for i in selected])
            return

        if n == len(data):
            return

        if sum(selected) > 20:
            return

        rec(data, selected + [n], n, m, callback)
        rec(data, selected, n+1, m, callback)

    rec(data, [], 0, m, callback)


d = list(range(1, 10))

def useSelections(lm):
    if sum(lm) == 20:
        global ans_cnt
        ans_cnt = ans_cnt + 1
        print(ans_cnt, lm)

for i in range(21):
    applyRepRecSelections(d, i, useSelections)

print(ans_cnt)