import heapq

class MedianFinder:

    def __init__(self):
        # max heap
        self.lesser_half = []
        # min heap
        self.greater_half = [] 
        

    def addNum(self, num: int) -> None:
        if not self.lesser_half or num <= -self.lesser_half[0]:
            heapq.heappush(self.lesser_half, -num)
        else:
            heapq.heappush(self.greater_half, num)
        if len(self.greater_half) - len(self.lesser_half) > 1:
            heapq.heappush(self.lesser_half, -heapq.heappop(self.greater_half))
        if len(self.lesser_half) - len(self.greater_half) > 1:
            heapq.heappush(self.greater_half, -heapq.heappop(self.lesser_half))

    def findMedian(self) -> float:
        if len(self.lesser_half) == len(self.greater_half):
            return (-self.lesser_half[0] + self.greater_half[0]) / 2
        elif len(self.lesser_half) > len(self.greater_half):
            return -self.lesser_half[0]
        else:
            return self.greater_half[0]
        