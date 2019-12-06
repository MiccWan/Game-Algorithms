import math
from collections import Counter

primeTable = []

def buildTable(n):
    newTable = [True] * (n + 1)
    newTable[0] = False
    newTable[1] = False
    for i in range(2, n):
        if newTable[i]:
            for j in range(i*i, n + 1, i):
                newTable[j] = False
    global primeTable
    primeTable = newTable

# buildTable(97)
# print([i for i in range(len(primeTable)) if primeTable[i]])


def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False

    for i in range(5, math.floor(math.sqrt(n) + 1), 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
    return True

def factorization(n):
    cnt = Counter()
    for i in range(2, math.floor(math.sqrt(n) + 1)):
        if i > n:
            break
        while n % i == 0:
            n /= i
            cnt[i] += 1
    if n > 1:
        cnt[int(n)] += 1
    return cnt