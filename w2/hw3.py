n = 9

def test(l):
    if len(l) != 9:
        raise Exception("Invalid permutation.")
    else:
        if not (l[0] + l[1] - l[2] == 4):
            return
        if not ((l[3] - l[4]) * l[5] == 4):
            return
        if not (l[6] + l[7] - l[8] == 4):
            return
        if not ((l[0] + l[3]) / l[6] == 4):
            return
        if not ((l[1] - l[4]) * l[7] == 4):
            return
        if not (l[2] - l[5] - l[8] == 4):
            return
        print("{}, {}, {}\n{}, {}, {}\n{}, {}, {}".format(*l))

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