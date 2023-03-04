from collections import Counter


class Solution:
    def majorityElement(self, nums):
        n = len(nums) / 2
        dict = Counter(nums)
        for i in range(len(nums)):
            if dict[nums[i]] > n:
                return nums[i]


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    a = Solution()
    print(a.majorityElement(nums))
