# 252. Meeting Rooms
#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals.sort(key = lambda i : i.start)

        for i in range(1, len(intervals)):
            prev_it = intervals[i - 1]
            curr_it = intervals[i]
