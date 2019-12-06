n = 9

ans_cnt = 0

def test(l):
    global ans_cnt
    if len(l) != 9:
        raise Exception("Invalid permutation.")
    else:
        a = l[0] + l[1] + l[2] + l[3]
        b = l[3] + l[4] + l[5] + l[6]
        c = l[6] + l[7] + l[8] + l[0]
        if not (a == b and b == c and c == a):
            return
        # print("   {}   \n  {} {}  \n {}   {} \n{} {} {} {} line sum = {}\n".format(*l, a))
        ans_cnt = ans_cnt + 1

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