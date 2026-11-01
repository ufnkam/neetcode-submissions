class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not coins: return 0
        memo = {}
        return self._dp(0, amount, memo, coins)

    def _dp(
        self, 
        index: int,
        remaining: int,
        memo: dict[tuple[int, int], int],
        coins: list[int],
    ) -> int:
        if remaining == 0: return 1
        if index == len(coins) or remaining < 0: return 0 
        if (index, remaining) in memo: return memo[(index, remaining)]
        take = self._dp(index, remaining - coins[index], memo, coins)
        skip = self._dp(index + 1, remaining, memo, coins)
        memo[(index, remaining)] = take + skip
        return memo[(index, remaining)]
            