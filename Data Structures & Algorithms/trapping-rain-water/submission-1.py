class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        vol = 0
        peak = height.index(max(height))
        l, r = 0, 1

        while r <= peak:
            if height[l] == 0:
                l += 1
                r += 1
                continue
            if height[r] >= height[l]:
                l = r
                r += 1
                continue
            vol += height[l] - height[r] 
            r += 1

        r = n - 1
        l = n - 2
        while l >= peak:
            if height[r] == 0:
                l -= 1
                r -= 1
                continue
            if height[l] >= height[r]:
                r = l
                l -= 1
                continue
            vol += height[r] - height[l] 
            l -= 1

        return vol