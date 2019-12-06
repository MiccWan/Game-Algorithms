# must set list l manually
l = [1, 1, 2, 2, 5, 6, 7, 8, 9]

ans_cnt = 0

def test(l):
    global ans_cnt

    a = l[0]
    b = l[1] * 10 + l[2]
    c = l[3]
    d = l[4] * 10 + l[5]
    e = l[6]
    f = l[7] * 10 + l[8]
    if not (a*d*f + c*b*f + e*b*d == b*d*f):
        return

    print("{} / {} + {} / {} + {} / {} = 1".format(a, b, c, d, e, f))
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