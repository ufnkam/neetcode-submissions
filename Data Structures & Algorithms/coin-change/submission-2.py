class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)
        val = self._backtrack(
            coins,
            amount,
            memo,
        )
        return val if val < float('inf') else -1
        
    def _backtrack(
        self,
        coins: list[int],
        remaining: int,
        memo: list[int],
    ) -> int:
        if remaining == 0:
            return 0

        if remaining < 0:
            return float('inf')

        if memo[remaining] != -1:
            return memo[remaining]

        best = float('inf')
        for coin in coins:
            best = min(
                1 + self._backtrack(coins, remaining - coin, memo), best
            )

        memo[remaining] = best
        return best


        