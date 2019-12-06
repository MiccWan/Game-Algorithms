n = 9

def test(l):
    if len(l) != 9:
        raise Exception("Invalid permutation.")
    else:
        a = l[0] * 10 + l[1]
        b = l[2]
        c = l[3] * 10 + l[4]
        d = l[5] * 10 + l[6]
        e = l[7] * 10 + l[8]
        if not a * b == c:
            return
        if not c + d == e:
            return
        print("{} * {} = {}, {} + {} = {}".format(a, b, c, c, d, e))
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