class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        target = 0
        nums = sorted(nums)

        triplets = set()
        for i in range(n):
            complement = -nums[i]

            slow, fast = i + 1, n - 1
            while slow < fast:
                the_sum = nums[slow] + nums[fast]
                if the_sum == complement:
                    triplets.add((nums[i], nums[slow], nums[fast]))
                    slow += 1
                    fast -= 1
                elif the_sum > complement:
                    fast -= 1
                elif the_sum < complement:
                    slow += 1

        return list(triplets) 