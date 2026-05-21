"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        interval_times = [[interval.start, interval.end] for interval in intervals]
        interval_times.sort()

        min_heap = []
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, interval_times[0][-1])

        for i in range(1, len(interval_times)):
            if interval_times[i][0] < min_heap[0]:
                heapq.heappush(min_heap, interval_times[i][-1])
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, interval_times[i][-1])
        
        return len(min_heap)