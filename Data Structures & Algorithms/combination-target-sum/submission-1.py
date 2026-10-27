class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs, curr_comb = [], []
        self._backtrack(nums, target, 0, curr_comb, combs, 0)
        return combs

    def _backtrack(
        self,
        nums: list[int],
        target: int,
        index: int,
        curr_comb: list[int],
        combs: list[list[int]],
        current_val: int,
    ) -> None:
        if index == len(nums):
            if current_val == target:
                combs.append(curr_comb.copy())
            return

        if current_val > target:
            return
        # skip
        self._backtrack(
            nums, target, index + 1, curr_comb, combs, current_val
        )
        # take
        curr_comb.append(nums[index])
        self._backtrack(nums, target, index, curr_comb, combs, current_val + nums[index])
        curr_comb.pop()

        


        

            