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
            if curr_it.start < prev_it.end:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    print("Output is:", sol.canAttendMeetings(intervals))  # Expected False [web:2][web:4][web:6]
