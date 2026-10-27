class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        combs, curr_comb = [], []
        self._backtrack(nums, 0, curr_comb, combs)
        return combs

    def _backtrack(
        self, 
        nums: list[int],
        index: int,
        curr_comb: list[int],
        combs: list[list[int]]
    ) -> None:
        if index == len(nums):
            combs.append(curr_comb.copy())
            return

        # skip
        new_index = index
        while new_index < len(nums) and nums[new_index] == nums[index]:
            new_index += 1
        self._backtrack(nums, new_index, curr_comb, combs)
        # take
        curr_comb.append(nums[index])
        self._backtrack(nums, index + 1, curr_comb, combs)
        curr_comb.pop()