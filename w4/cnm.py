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

def solve(l, h = []):
    if h == []:
        h = list(map(lambda x: str(x), l))
        print("Solving {}...".format(l))

    if len(l) == 1:
        return(abs(l[0] - 30) < 0.0001, h, False)

    best_res = (False, "Whatever", True)

    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            combs = []
            combs.append((l[i] + l[j], "{} + {}".format(h[i], h[j])))
            combs.append((l[i] * l[j], "({}) * ({})".format(h[i], h[j])))
            combs.append((l[i] - l[j], "{} - ({})".format(h[i], h[j])))
            combs.append((l[j] - l[i], "{} - ({})".format(h[j], h[i])))
            if l[j] != 0:
                combs.append((l[i] / l[j], "({}) / ({})".format(h[i], h[j])))
            if l[i] != 0:
                combs.append((l[j] / l[i], "({}) / ({})".format(h[j], h[i])))

            for comb_v, comb_h in combs:
                used_decimal = False
                if not isinstance(comb_v, int):
                    if not comb_v.is_integer():
                        used_decimal = True
                sl = [comb_v] + l[:i] + l[i+1:j] + l[j+1:]
                sh = [comb_h] + h[:i] + h[i+1:j] + h[j+1:]
                next = solve(sl, sh)
                
                if next[0]:
                    if not used_decimal:
                        if not next[2]:
                            if len(l) == 5:
                                print("{}, used decimal: {}\n".format(next[1][0], next[2]))
                            return(next)

                    best_res = (next[0], next[1], True)

    if best_res[0]:
        if len(l) == 5:
            print("{}, used decimal: {}\n".format(best_res[1][0], best_res[2]))
        return(best_res)
    if len(l) == 5:
        print("No solution.\n")
    return(False, h, False)

ans_cnt = 0
need_decimal_ans_cnt = 0

def useSelections(lm):
    global ans_cnt
    global need_decimal_ans_cnt
    res = solve(lm)
    if res[0]:
        ans_cnt += 1
    if res[2]:
        need_decimal_ans_cnt += 1

solve([8,9,10,12,13])
#applySelections(list(range(1,14)), 5, useSelections)
print("ans_cnt =", ans_cnt)
print("need decimal =", need_decimal_ans_cnt)

