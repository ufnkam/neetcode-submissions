class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        memo = [-1] * n
        result = 1
        for i in range(n):
            result = max(result, self._dp(i, nums, memo))

        return result

    def _dp(
        self,
        i: int,
        nums: list[int],
        memo: list[int],
    ) -> int:
        if memo[i] != -1:
            return memo[i]

        memo[i] = 1
        for j in range(i):
            if nums[j] < nums[i]:
                memo[i] = max(memo[i], 1 + self._dp(j, nums, memo))

        return memo[i]
                