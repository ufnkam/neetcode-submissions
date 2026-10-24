class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        slow, fast = 0, n - 1

        biggest_container = 0
        while slow < fast:
            slowh = heights[slow]
            fasth = heights[fast]
            
            dist = fast - slow
            current_h = 0
            if slowh > fasth:
                current_h = fasth
            elif slowh < fasth:
                current_h = slowh
            else:
                current_h = slowh

            area = current_h * dist
            biggest_container = max(biggest_container, area)

            if slowh < fasth:
                slow += 1
            elif fasth < slowh:
                fast -= 1
            else:
                slow += 1

        return biggest_container