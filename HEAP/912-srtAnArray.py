import heapq


class Solution:
    def sortArray(self, nums):
        ans = []
        heap = []
        for num in nums:
            heapq.heappush(heap, num)

        for i in range(len(heap)):
            a = heapq.heappop(heap)
            ans.append(a)
        return ans


if __name__ == '__main__':
    nums = [5, 2, 3, 1]
    a = Solution()
    print(a.sortArray(nums))
