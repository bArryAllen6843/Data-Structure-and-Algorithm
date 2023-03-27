import heapq


class Solution:
    def lastStoneWeight(self, stones) -> int:
        heap = []
        for el in stones:
            heapq.heappush(heap, -el)

        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 != stone2:
                stone1 = stone1 - stone2
                if stone1 > 0:
                    heapq.heappush(heap, -stone1)
        return -heapq.heappop(heap) if len(heap) == 1 else 0


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    a = Solution()
    print(a.lastStoneWeight(stones))
