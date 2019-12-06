def swap(l, a, b):
    l[a], l[b] = l[b], l[a]
    return l

def is_odd(s):
    cnt = 0
    for i, num in enumerate(s, start=1):
        cnt += sum(num>num2 for num2 in s[i:]) 
    return cnt % 2

def heaps(a, n):

    if n == 1:
        if not is_odd(a):
            print(a)
        return

    for i in range(n-1):
        heaps(a, n-1)
        if n % 2 == 0:
            a = swap(a, n-1, i)
        else:
            swap(a, n-1, 0)
    heaps(a, n-1)

n = int(input("n = "))

l = list(range(1, 1+n))

heaps(l, len(l))