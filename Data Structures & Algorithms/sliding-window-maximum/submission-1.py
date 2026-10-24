import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        n = len(nums)
        start = 0
        maxes = []
        heap = [(-num, i) for i, num in enumerate(nums) if i < k - 1]
        heapq.heapify(heap)
        for end in range(k - 1, n):
            heapq.heappush(heap, (-nums[end], end))
            # drop index out of the window
            while heap[0][1] < start:
                heapq.heappop(heap) 
            maxes.append(-heap[0][0])
            start += 1

        return maxes