import heapq


class Solution:
    def maxProduct(self, nums):
        heap = [-1]
        for num in nums:
            if num > heap[0]:
                if len(heap) == 2:
                    heapq.heappop(heap)
                heapq.heappush(heap, num)
        return (heap[0] - 1) * (heap[1] - 1)


if __name__ == '__main__':
    num = [3, 4, 5, 2]
    a = Solution()
    print(a.maxProduct(num))
