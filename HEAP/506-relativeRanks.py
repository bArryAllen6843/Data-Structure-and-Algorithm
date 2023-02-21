import heapq


class Solution:
    def findRelativeRanks(self, score):
        heap = []
        for i, el in enumerate(score):
            heapq.heappush(heap, (-el, i))
        ans = [''] * len(score)
        r = 1
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        while len(heap) != 0:
            _, i = heapq.heappop(heap)
            if r <= 3:
                ans[i] = rank[r - 1]
            else:
                ans[i] = f'{r}'
            r += 1
        return ans


if __name__ == '__main__':
    # score = [5, 4, 3, 2, 1]
    score = [10, 3, 8, 9, 4]
    a = Solution()
    print(a.findRelativeRanks(score))
