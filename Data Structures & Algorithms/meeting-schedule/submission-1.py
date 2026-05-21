"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        interval_times = []

        for interval in intervals:
            interval_times.append([interval.start, interval.end])
        
        interval_times.sort()

        for i in range(1, len(interval_times)):
            if interval_times[i][0] < interval_times[i - 1][-1]:
                return False
        
        return True
