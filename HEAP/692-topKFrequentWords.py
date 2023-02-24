import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words, k: int):
        freq = Counter(words)
        heap = []

        for el in freq:
            count = freq[el]
            heapq.heappush(heap, (-count, el))

        ans = []
        for i in range(k):
            cnt, el = heapq.heappop(heap)
            ans.append(el)
        return ans


if __name__ == '__main__':
    # words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    # k = 4
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2

    a = Solution()
    print(a.topKFrequent(words, k))
