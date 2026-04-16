class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = -Infinity;
        let l = 0
        let r = 1
        while (r < prices.length) {
            if (prices[r] < prices[l]) {
                l = r;
            } else {
                const profit = prices[r] - prices[l];
                console.debug({profit,maxProfit})
                maxProfit = Math.max(profit, maxProfit);
            }
            r++;
        }
        if (maxProfit < 0) {
            return 0
        }
        return maxProfit



    }
}
