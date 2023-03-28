class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxCount = max(maxCount, count)
            else:
                maxCount = max(maxCount, count)
                count = 0
        return maxCount


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    a = Solution()
    print(a.findMaxConsecutiveOnes(nums))
