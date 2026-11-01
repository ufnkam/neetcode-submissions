class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        target = total // 2
        memo = {}
        return self._dp(0, target, nums, memo)

    def _dp(
        self,
        index: int,
        remaining: int,
        nums: list[int],
        memo: dict[tuple[int, int], bool],
    ) -> bool:
        if remaining == 0: return True
        if index == len(nums) or remaining < 0: return False
        if (index, remaining) in memo: return memo[(index, remaining)]
        take = self._dp(index + 1, remaining - nums[index], nums, memo)
        skip = self._dp(index + 1, remaining, nums, memo)
        memo[(index, remaining)] = take or skip
        return memo[(index, remaining)]
