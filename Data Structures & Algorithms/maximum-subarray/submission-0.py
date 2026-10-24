class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        window_sum = 0
        best = float('-inf')

        for end in range(len(nums)):
            if window_sum < 0:
                window_sum = 0
            
            window_sum += nums[end]
            best = max(window_sum, best)

        return best