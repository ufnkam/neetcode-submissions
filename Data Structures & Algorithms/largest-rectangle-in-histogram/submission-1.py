class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        stack = []
        max_area = 0
        min_height = 0
        n = len(heights)
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                h = stack.pop()
                right = stack[-1] if stack else n
                max_area = max(max_area, heights[h] * (right - i - 1))
 
            stack.append(i)

        while stack:
            h = stack.pop()
            right = stack[-1] if stack else n
            max_area = max(max_area, heights[h] * right)

        return max_area