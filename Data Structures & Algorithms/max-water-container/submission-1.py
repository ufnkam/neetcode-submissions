class Solution:
    def maxArea(self, heights: List[int]) -> int:
        slow, fast = 0, len(heights) - 1
        max_area = 0

        while slow < fast:
            dist = fast - slow
            
            if heights[slow] > heights[fast]:
                height = heights[fast]
                fast -= 1
            else:
                height = heights[slow]
                slow += 1

            area = dist * height
            max_area = max(max_area, area)



        return max_area