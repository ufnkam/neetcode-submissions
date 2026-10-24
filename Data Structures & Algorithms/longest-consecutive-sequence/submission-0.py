class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                looking_for = num + 1
                while looking_for in num_set:
                    looking_for += 1
                    length += 1
                longest = max(longest, length)

        return longest



