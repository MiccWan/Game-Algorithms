# must set list l manually
l = [1, 1, 2, 2, 5, 6, 7, 8, 9]

ans_cnt = 0

def test(l):
    global ans_cnt
    a = l[0] * 10000 + l[1] * 1000 + l[2] * 100 + l[3] * 10 + l[4]
    b = l[5] * 1000 + l[6] * 100 + l[7] * 10 + l[8]
    if not (a - b == 33333):
        return
    print("{} - {} = 33333".format(a, b))
    ans_cnt = ans_cnt + 1

def swap(l, a, b):
    l[a], l[b] = l[b], l[a]
    return l

def decSwapAlg(l, n, callback):

    while True:

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

l.sort()
decSwapAlg(l, len(l), test)
print("Ans count = {}".format(ans_cnt))