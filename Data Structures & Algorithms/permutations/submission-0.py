class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combs, curr_comb = [], []
        used = [False] * len(nums)
        self._backtrack(nums, 0, curr_comb, combs, used)
        return combs

    def _backtrack(
        self,
        nums: list[int],
        index: int,
        curr_comb: list[int],
        combs: list[list[int]],
        used: list[bool],
    ) -> None:
        if index == len(nums):
            combs.append(curr_comb.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                curr_comb.append(nums[i])
                used[i] = True
                self._backtrack(nums, index + 1, curr_comb, combs, used)
                used[i] = False
                curr_comb.pop()

        
