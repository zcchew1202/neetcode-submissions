class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = float('-inf')
        for r in range(1,len(prices)):
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
            if prices[l] > prices[r]:
                print(profit,maxProfit)
                l = r
        return maxProfit if maxProfit > 0 else 0 

