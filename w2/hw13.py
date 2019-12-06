from time import time
ans_cnt = 0

def toNum(l):
    from functools import reduce
    return reduce(lambda x,y: 10*x+y, l)

def test(l):
    global ans_cnt

    a = toNum(l[:4])
    b = toNum(l[4:])
    c = toNum(reversed(l[4:]))
    d = toNum(reversed(l[:4]))

    if not (a*b == c*d):
        return

    print("Answer founded: {} * {} = {} * {}".format(a, b, c, d))

    ans_cnt = ans_cnt + 1

def swap(l, a, b):
    l[a], l[b] = l[b], l[a]
    return l

def decSwapAlg(l, n, callback):
    cnt = 0
    while True:
        cnt = cnt + 1
        if cnt % 36288==0:
            print("{}% finished.".format(cnt / 36288))
            pass
        callback(l)

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

        l = swap(l, i, j)

        l[i+1:] = l[i+1:][::-1]

# l = list(range(10))
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
s_time = time()
decSwapAlg(l, len(l), test)
print("Process finished in {} seconds.".format(time() - s_time))
print("Ans count = {}\n".format(ans_cnt))
