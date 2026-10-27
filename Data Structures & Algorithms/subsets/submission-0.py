class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        comb, curr_comb = [], []
        self._backtrack(nums, 0, curr_comb, comb)
        return comb
    def _backtrack(
        self, 
        nums: list[int],
        index: int,
        curr_comb: list[int],
        combs: list[list[int]],
    ) -> None:
        if index == len(nums):
            combs.append(curr_comb.copy())
            return
        
        # skip
        self._backtrack(nums, index + 1, curr_comb, combs)
        # add
        curr_comb.append(nums[index])
        self._backtrack(nums, index + 1, curr_comb, combs)
        curr_comb.pop()