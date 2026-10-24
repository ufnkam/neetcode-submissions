"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.end)

        overlap = 0
        prev_end = float('-inf')

        for i in intervals:
            if i.start >= prev_end:
                prev_end = i.end
                continue
            
            overlap += 1

        return overlap == 0