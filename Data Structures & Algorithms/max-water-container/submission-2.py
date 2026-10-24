class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        max_area = 0

        while l < r:
            dist = r - l
            if heights[l] >= heights[r]:
                height = heights[r]
                r -= 1
            else:
                height = heights[l]
                l += 1

            current = dist * height
            max_area = max(max_area, current) 

        return max_area