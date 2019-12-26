def findLongestCycle(n = 30):

    availableNum = [True] * (n + 1)
    nextNum = [list(range(1, n + 1))]

    # init nextNum
    for i in range(1, n + 1):
        nextNumArr = []
        for j in range(1, n + 1):
            if (j % i == 0) or (i % j == 0):
                nextNumArr.append(j)
        nextNum.append(nextNumArr)

    # for i in range(1, n+1):
    #     print(i, nextNum[i])

    def getAns(now = 0, depth = 0):
        ans = 0
        added = False
        for i in nextNum[now]:
            if availableNum[i]:
                added = True
                availableNum[i] = False
                ans = max(ans, getAns(i, depth + 1))
                if now == 0:
                    print((i / n * 100) // 0.1 * 0.1, "% finished.")
                availableNum[i] = True
        if not added:
            return depth
        return ans

    return getAns()

# print(findLongestCycle(7))
# print(findLongestCycle(12))
# print(findLongestCycle(15))
print(findLongestCycle(30))
