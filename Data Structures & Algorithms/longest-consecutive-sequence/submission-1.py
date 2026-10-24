class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        hashset = set(nums)
        current = 0

        for num in nums:
            if not num - 1 in hashset:
                current = 1 
                while num + 1 in hashset:
                    current += 1
                    num = num + 1
                best = max(current, best)
                current = 0
            
        return best
