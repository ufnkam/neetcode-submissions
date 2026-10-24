class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs, curr_comb = [], []
        self._backtrack(
            nums,
            0,
            curr_comb,
            combs,
            target,
            0
        )
        return combs

    def _backtrack(
        self,
        nums: list[int],
        index: int,
        curr_comb: list[int],
        combs: list[list[int]],
        target: int,
        curr_val: int,
    ) -> None:
        if index == len(nums):
            if curr_val == target:
                combs.append(curr_comb.copy())
            return

        if curr_val > target:
            return

        # we will try another one
        self._backtrack(
            nums,
            index + 1,
            curr_comb,
            combs,
            target, 
            curr_val
        )

        # add to set
        curr_val += nums[index]
        curr_comb.append(nums[index])
        self._backtrack(
            nums,
            index,
            curr_comb,
            combs,
            target,
            curr_val
        )
        curr_comb.pop()
        curr_val -= nums[index]

        

            