import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        res, c = [], Counter(s)
        prevA, prevB = 0, ''
        heap = [(-value, key) for key, value in c.items()]
        heapq.heapify(heap)

        while heap:
            a, b = heapq.heappop(heap)
            res += [b]

            # if count of a is more than -1 then we will push it again into heap for later pop
            if prevA < 0:
                heapq.heappush(heap, (prevA, prevB))

            # decreasing count of b by increasing a(as a is negative)
            a += 1
            prevA, prevB = a, b
        res = ''.join(res)
        if len(res) != len(s): return ""
        return res


if __name__ == '__main__':
    s = "aab"
    a = Solution()
    print(a.reorganizeString(s))
