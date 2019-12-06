l = [1, 0, 0, 1, 0]
ans = []

def l2num(l):
    r = 0
    for i in l:
        r *= 2
        r += i
    return r

def solve(l):
    global ans
    f = [0] * len(l)
    while l != f:
        print(l)
        ans.append(str(l2num(l)))
        if sum(l) % 2 == 1:
            l[-1] = l[-1] ^ 1
        else:
            index = 0
            for i in reversed(range(len(l))):
                if l[i] != 0:
                    index = i - 1
                    break
            l[index] = l[index] ^ 1
    ans.append("0")

def solve2(l):
    f = [0] * len(l)
    while l != f:
        l2 = [0] + l[:-1]
        print(l2num(l))
        print(l)
        print(l2)
        l = [l[i] ^ l2[i] for i in range(len(l))]


solve(l.copy())
# solve2(l.copy())
print(",".join(ans))
