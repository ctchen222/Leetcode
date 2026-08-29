from collections import deque


# This is the solution when you need to consider additional return values, such as the range of the maximum profit.
def getMaxProfitWithRange(pnl, k):
    n = len(pnl)
    if n == 0 or k <= 0:
        return 0, (-1, -1)

    # prefix calculate
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + pnl[i]
    
    ans = float('-inf')
    lbest, rbest = -1, -1

    dq = deque()
    dq.append(0)

    for r in range(1, n+1):
        # r - l <= k => l < r - k
        while dq and dq[0] < r - k:
            dq.popleft()

        # check current window sum and replace with ans if sum(window) < ans
        cur = prefix[r] - prefix[dq[0]]
        if cur > ans:
            ans = cur
            rbest, lbest = r - 1, dq[0]


        while dq and prefix[r] <= prefix[dq[-1]]:
            dq.pop()
        dq.append(r)
    
    return ans, (lbest, rbest)


tests = [
    # pnl, k, expected_sum, expected_range
    ([3, -2, 5, -1], 2, 5, (2, 2)),
    ([4, -1, 2, 1], 2, 4, (0, 0)),
    ([1, 2, 3, -10, 4], 3, 6, (0, 2)),
    ([-5, -2, -8], 2, -2, (1, 1)),
    ([1, 2, 3, 4], 2, 7, (2, 3)),
    ([5, -100, 6, 7], 2, 13, (2, 3)),
    ([-10, 4, 3, -2, 1], 3, 7, (1, 2)),
    ([2, -1, 7, 3], 1, 7, (2, 2)),
    ([2, -1, 3], 10, 4, (0, 2)),
]


for pnl, k, expected_sum, expected_range in tests:
    got_sum, got_range = getMaxProfitWithRange(pnl, k)
    print(
        pnl, k,
        "got:", (got_sum, got_range),
        "expected:", (expected_sum, expected_range)
    )
    assert(got_sum == expected_sum and got_range == expected_range)

