class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                curProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, curProfit)
            else:
                l = r
            r += 1
        return maxProfit
