class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [1] * n
        for i in range(1, n):
            prod[i] = prod[i - 1] * nums[i - 1]

        right = 1
        for i in range(n - 1, -1, -1):
            prod[i] = prod[i] * right
            right = right * nums[i]

        return prod