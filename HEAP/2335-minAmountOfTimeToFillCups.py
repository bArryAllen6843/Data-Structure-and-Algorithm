import heapq


class Solution:
    def fillCups(self, amount):
        heap = []

        for a in amount:
            heapq.heappush(heap, -a)
        seconds = 0
        while heap[0] != 0:
            max1 = heapq.heappop(heap)
            max2 = heapq.heappop(heap)
            seconds += 1
            heapq.heappush(heap, max1 + 1)
            heapq.heappush(heap, max2 + 1)
        return seconds


if __name__ == '__main__':
    amount = [1, 4, 2]
    a = Solution()
    print(a.fillCups(amount))
