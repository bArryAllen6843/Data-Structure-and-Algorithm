import heapq


class Solution:
    def maxSubsequence(self, nums, k: int):
        heap = []
        for i, val in enumerate(nums):
            if len(heap) == k:
                heapq.heappushpop(heap, (val, i))
            else:
                heapq.heappush(heap, (val, i))

        heap.sort(key=lambda x: x[1])
        ans = []

        for i in heap:
            ans.append(i[0])
        return ans


if __name__ == '__main__':
    nums = [2, 1, 3, 3]
    k = 2
    a = Solution()
    print(a.maxSubsequence(nums, k))
