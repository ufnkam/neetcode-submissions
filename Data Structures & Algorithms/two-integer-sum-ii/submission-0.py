class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        slow, fast = 0, n - 1
        
        while slow < fast:
            the_sum = numbers[slow] + numbers[fast] 
            if the_sum == target:
                return [slow + 1, fast + 1]

            if the_sum > target:
                fast -= 1

            if the_sum < target:
                slow += 1

        return []
