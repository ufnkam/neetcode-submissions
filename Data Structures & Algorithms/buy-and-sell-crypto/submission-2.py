class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        profit = 0
        l, r = 0, 1
        while r < n:
            curr_prof = prices[r] - prices[l]
            profit = max(curr_prof, profit)
            if curr_prof < 0:
                l += 1
                continue
            r += 1

        return profit
        