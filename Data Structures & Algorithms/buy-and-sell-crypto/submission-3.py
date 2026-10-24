class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        profit = 0
        l, r = 0, 1
        while r < n:
            if prices[l] > prices[r]:
                l = r 
            curr_prof = prices[r] - prices[l]
            profit = max(curr_prof, profit)

            r += 1

        return profit
        