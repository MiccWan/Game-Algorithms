import time

ans_cnt = 0

def test(l, ln):
    global ans_cnt

    for i in range(ln):
        if i != ln-1:
            if l[i] > l[i+1]:
                return
            if l[i+ln] > l[i+ln+1]:
                return
        if l[i] > l[i+ln]:
            return
    ans_cnt = ans_cnt + 1
    # print("\n", a, "\n", b)

def swap(l, a, b):
    l[a], l[b] = l[b], l[a]
    return l

def decSwapAlg(l, n, callback):
    ln = int(n / 2)
    cnt = 0
    global ans_cnt
    start_time = time.time()
    while True:

        if l[0] != 1:
            print("Tried all 1xxxxxxxxx.")
            print("l =", l)
            return

        cnt = cnt + 1
        if cnt % 4790016 == 0:
            print("{}% finished, {} solutions founded, {} seconds spent.".format(cnt/4790016, ans_cnt, time.time() - start_time))
            start_time = time.time()
        callback(l, ln)

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

for i in range(6, 7):
    print("n =", i)
    ans_cnt = 0
    l = list(range(1, 2 * i + 1))
    decSwapAlg(l, len(l), test)
    print("Ans count = {}\n".format(ans_cnt))

