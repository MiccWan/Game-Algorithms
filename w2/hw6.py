n = 9

ans_cnt = 0

def test(l):
    global ans_cnt
    if len(l) != 9:
        raise Exception("Invalid permutation.")
    else:
        a = l[0]
        b = l[1] * 10 + l[2]
        c = l[3] * 100 + l[4] * 10 + l[5]
        d = l[6] * 100 + l[7] * 10 + l[8]

        if not (a + b + c == d):
            return
        ans_cnt = ans_cnt + 1
        print("{} -> {} + {} + {} = {}".format(ans_cnt, a, b, c, d))

def swap(l, a, b):
    l[a], l[b] = l[b], l[a]
    return l

def heaps(a, n, callback):

    if n == 1:
        callback(a)
        return

    for i in range(n-1):
        heaps(a, n-1, callback)
        if n % 2 == 0:
            a = swap(a, n-1, i)
        else:
            swap(a, n-1, 0)
    heaps(a, n-1, callback)

l = list(range(1, 1+n))

heaps(l, len(l), test)

print(ans_cnt)