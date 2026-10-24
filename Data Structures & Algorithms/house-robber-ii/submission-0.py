class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[1], nums[0])

        return max(
            self.rob_in_line(nums[:-1]),
            self.rob_in_line(nums[1:])
        )

    @staticmethod
    def rob_in_line(
        nums: int
    ) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[1], nums[0])
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[n - 1]