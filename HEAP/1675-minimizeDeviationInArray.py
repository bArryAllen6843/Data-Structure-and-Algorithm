import heapq


class Solution:
    def minimumDeviation(self, nums):
        heap = []
        for num in nums:
            tmp = num
            while tmp % 2 == 0: tmp //= 2
            heap.append((tmp, max(num, tmp * 2)))

        Max = max(i for i, j in heap)
        heapq.heapify(heap)
        ans = float("inf")

        while len(heap) == len(nums):
            num, limit = heapq.heappop(heap)
            ans = min(ans, Max - num)
            if num < limit:
                heapq.heappush(heap, (num * 2, limit))
                Max = max(Max, num * 2)

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # nums = [4, 1, 5, 20, 3]
    a = Solution()
    print(a.minimumDeviation(nums))
