def swap(l, a, b):
    l[a], l[b] = l[b], l[a]
    return l

def heaps(a, n):

    if n == 1:
        print(a)
        return

    for i in range(n-1):
        heaps(a, n-1)
        if n % 2 == 0:
            a = swap(a, n-1, i)
        else:
            swap(a, n-1, 0)
    heaps(a, n-1)

# n = int(input("n = "))

# l = list(range(1, 1+n))

heaps([0,1,1,2], 4)