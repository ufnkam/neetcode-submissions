class Solution:
    def trap(self, height: List[int]) -> int:
        size = 0
        n = len(height)
        peak = height.index(max(height))
        l, r = 0, 0 + 1

        while r <= peak:
            if height[l] == 0:
                l += 1
                r += 1
                continue

            if height[r] >= height[l]:
                l = r
                r += 1
                continue

            size += height[l] - height[r]
            r += 1  

        r = n - 1 
        l = n - 2
        while l >= peak:
            if height[r] == 0:
                r -= 1
                l -= 1
                continue
            
            if height[l] >= height[r]:
                r = l
                l -= 1
                continue

            size += height[r] - height[l]
            l -= 1

        return size    