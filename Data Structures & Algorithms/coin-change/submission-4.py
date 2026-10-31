class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = [-1] * (amount + 1)
        val = self._backtrack(amount, coins, memo)
        return val if val < float('inf') else -1

    def _backtrack(
        self,
        remaining: int,
        coins: list[int],
        memo: list[int]
    ) -> int:
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        if memo[remaining] != -1:
            return memo[remaining]
        
        best = float('inf')
        for coin in coins:
            new_val = 1 + self._backtrack(remaining - coin, coins, memo)
            best = min(best, new_val)
        
        memo[remaining] = best
        return best

        