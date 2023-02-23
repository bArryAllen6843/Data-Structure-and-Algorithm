import heapq
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        heap = []
        ans = ""
        for el in freq:
            count = freq[el]
            heapq.heappush(heap, (-count, el))
        for i in range(len(heap)):
            count, el = heapq.heappop(heap)
            ans += el * (-count)

        return ans


if __name__ == '__main__':
    s = "tree"
    a = Solution()
    print(a.frequencySort(s))
