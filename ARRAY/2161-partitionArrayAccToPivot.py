class Solution:
    def pivotArray(self, nums, pivot: int):
        ans, pivot_freq = [], 0

        for num in nums:
            if num < pivot:
                ans.append(num)
            elif num == pivot:
                pivot_freq += 1

        ans.extend([pivot] * pivot_freq)

        for num in nums:
            if num > pivot:
                ans.append(num)

        return ans


if __name__ == '__main__':
    nums = [9, 12, 5, 10, 14, 3, 10]
    pivot = 10
    a = Solution()
    print(a.pivotArray(nums, pivot))
