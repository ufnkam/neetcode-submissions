class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            val = target - (nums[l] + nums[r])
            if val == 0:
                return [l + 1, r + 1]

            if val > 0:
                l += 1
            elif val < 0:
                r -= 1

        return []


        

