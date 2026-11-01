class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        best = 1
        memo = [-1] * n
        for i in range(n):
            best = max(best, self._dp(i, nums, memo))
        return best

    def _dp(
        self,
        index: int,
        nums: list[int],
        memo: list[int],
    ) -> int:
        if memo[index] != -1: return memo[index]
        memo[index] = 1
        for j in range(index):
            if nums[j] < nums[index]:
                memo[index] = max(memo[index], 1 + self._dp(j, nums, memo))
        return memo[index]


                