class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        max_profit = 0
        for i in range(n):
            buy = prices[i]
            for nd in range(i + 1, n):
                max_profit = max(prices[nd] - buy, max_profit)

        return max_profit 
