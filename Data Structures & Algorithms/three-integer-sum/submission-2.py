class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums = sorted(nums)

        res = set()
        n = len(nums)
        

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif val > 0:
                    r -= 1
                else:
                    l += 1

        return list(res)