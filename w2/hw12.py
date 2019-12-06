ans_cnt = 0

def test(l):
    global ans_cnt
    n = int(len(l) / 2)
    a = l[:n]
    b = l[n:]
    
    for i in range(n):
        if i != n-1:
            if a[i] > a[i+1]:
                return
            if b[i] > b[i+1]:
                return
        if a[i] > b[i]:
            return
    ans_cnt = ans_cnt + 1
    # print("\n", a, "\n", b)

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

for i in range(1, 7):
    print("n =", i)
    ans_cnt = 0
    l = list(range(1, 2 * i + 1))
    heaps(l, len(l), test)
    print("Ans count =", ans_cnt, "\n")