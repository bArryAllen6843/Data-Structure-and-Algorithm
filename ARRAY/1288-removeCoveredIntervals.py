class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        n = len(intervals)
        count = n
        intervals.sort()
        l = intervals[0][0]
        h = intervals[0][1]
        for i in range(1, n):
            # if interval is inside low and high then decrease count of intrevals by 1
            if intervals[i][0] >= l and intervals[i][1] <= h:
                count -= 1
            # if l,h = 1,4 and intervals[i] = [2,8] in this case we need to update low and high this will not affect
            # our solution as intervals are sorted according to low so if we got a new high then update l and h
            elif intervals[i][0] > l and intervals[i][1] > h:
                l = intervals[i][0]
                h = intervals[i][1]
            # if the intervals[i] is covering our low and high
            elif intervals[i][0] < l and intervals[i][1] > h:
                l = intervals[i][0]
                h = intervals[i][1]
            # in this case ex: l,h = 1,2 and intervals[i] = [1,4] we need to decrease count and update l and h
            elif intervals[i][0] == l and intervals[i][1] > h:
                count -= 1
                l = intervals[i][0]
                h = intervals[i][1]
        return count


if __name__ == '__main__':
    # intervals = [[1, 4], [3, 6], [2, 8]]
    intervals = [[1, 2], [1, 4], [3, 4]]
    a = Solution()
    print(a.removeCoveredIntervals(intervals))
