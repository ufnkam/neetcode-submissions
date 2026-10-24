class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        end = 0
        for i in range(n):
            if i > end:
                return False

            end = max(end, i + nums[i]) 

            if end >= n - 1:
                return True

        return True
