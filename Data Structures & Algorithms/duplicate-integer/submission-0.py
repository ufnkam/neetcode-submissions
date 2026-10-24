class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dedup = set(nums)
        return True if len(dedup) < len(nums) else False