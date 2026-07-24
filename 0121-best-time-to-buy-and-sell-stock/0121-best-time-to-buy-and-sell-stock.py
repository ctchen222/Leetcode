class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## Brute force
        # result = 0
        # n = len(prices)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         profit = prices[j] - prices[i]
        #         if profit >= result:
        #             result = profit
        # return result

        # O(n) solution
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit