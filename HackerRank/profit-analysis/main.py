from collections import deque


def getMaxProfit(pnl, k):
    n = len(pnl)

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + pnl[i]

    dq = deque()
    dq.append(0)

    ans = float('-inf')

    for r in range(1, n + 1):

        while dq and dq[0] < r - k:
            dq.popleft()

        ans = max(ans, prefix[r] - prefix[dq[0]])

        while dq and prefix[dq[-1]] >= prefix[r]:
            dq.pop()

        dq.append(r)

    return ans

# pnl =    [-3, 4, 3, -2, 2, 5]
# prefix = [0, -3, 1, 4, 2, 4, 9]
# k = 4


# print(getMaxProfit([-3, 4, 3, -2, 2, 5], 2))
# r = 1: dq = [0] ans = -3 dq' = [1]
# r = 2: dq = [1] ans =  4 dq' = [1, 2]
# r = 3: dq [1, 2] ans = 7 dq' = [1, 3]
# r = 4: dq = [3] ans = 7 dq' = [4]
# r = 5: dq = [4] ans = 7 dq' = [4]
# r = 6: dq = [4] ans = 7 dq' = [4]
assert(getMaxProfit([-3, 4, 3, -2, 2, 5], 2) == 7)

# print(getMaxProfit([-3, 4, 3, -2, 2, 5], 4))
assert(getMaxProfit([-3, 4, 3, -2, 2, 5], 4) == 8)
# print(getMaxProfit([-3, 4, 3, -2, 5, -10], 4))
assert(getMaxProfit([-3, 4, 3, -2, 5, -10], 4) == 10)
# print(getMaxProfit([-3, 4, 3, -2, 1, -10], 4))
assert(getMaxProfit([-3, 4, 3, -2, 1, -10], 4) == 7)


