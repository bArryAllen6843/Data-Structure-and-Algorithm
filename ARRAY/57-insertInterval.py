class Solution:
    # if first element of your interval[i] is greater than end then it will come in right or if the last element
    # of the interval[i] is smaller than start then it will come in left otherwise update in that interval only
    def insert(self, intervals, newInterval):
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for i in intervals:
            if i[1] < s:
                left += i,
            elif i[0] > e:
                right += i,
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return left + [[s, e]] + right


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    a = Solution()
    print(a.insert(intervals, newInterval))
