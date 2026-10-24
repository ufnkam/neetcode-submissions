class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x: x[1])
        prev_end = float('-inf')
        to_drop = 0

        for i in intervals:
            if i[0] >= prev_end:
                prev_end = i[1]
                continue

            to_drop += 1

        return to_drop

            