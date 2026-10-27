class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        curr_comb, combs = [], set()
        self._backtrack(candidates, target, 0, curr_comb, combs, 0)
        return [list(sol) for sol in combs]

    def _backtrack(
        self, 
        nums: list[int], 
        target: int,
        index: int,
        curr_comb: list[int],
        combs: set[tuple[int]],
        curr_val: int,
    ) -> None:
        if curr_val == target: 
            combs.add(tuple(curr_comb))
            return
        if curr_val > target or index == len(nums): return
        # skip
        new_index = index
        while new_index < len(nums) and nums[index] == nums[new_index]: 
            new_index += 1
        self._backtrack(nums, target, new_index, curr_comb, combs, curr_val)
        # take
        curr_comb.append(nums[index])
        self._backtrack(nums, target, index + 1, curr_comb, combs, curr_val + nums[index])
        curr_comb.pop()
        