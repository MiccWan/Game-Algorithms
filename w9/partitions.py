def getSelfConjugatePartitions(N):

    def p(n,m):
        if n == m:
            return 1 + p(n, m - 1)
        if (m == 0 or n < 0):
            return 0
        if (n == 0 or m == 1):
            return 1

        return p(n, m - 1) + p(n - m, m)

    return sum([p((N - i * i) >> 1, i) for i in range(1, N + 1) if (i * i <= N and not (N - i * i) % 2)])
    
    # i = 1
    # ans = 0
    # while i * i <= N:
    #     if (N - i * i) % 2 == 1:
    #         i += 1
    #         continue
    #     ans += p((N - i * i) >> 1, i)
    #     i += 1

    # return ans

print(getSelfConjugatePartitions(80))