import sys


class Solution:
    def findMinDifference(self, timePoints) -> int:
        for i, time in enumerate(timePoints):
            timePoints[i] = toMin(time)

        res = sys.maxsize
        timePoints.sort()
        for i in range(len(timePoints) - 1):
            res = min(res, (timePoints[i + 1] - timePoints[i]))

        res = min(res, 60 * 24 - timePoints[-1] + timePoints[0])
        return res


def toMin(time):
    time = time.split(":")
    res = (60 * int(time[0])) + int(time[1])
    return res


if __name__ == '__main__':
    timePoints = ["23:59", "00:00", "10:44"]
    a = Solution()
    print(a.findMinDifference(timePoints))
