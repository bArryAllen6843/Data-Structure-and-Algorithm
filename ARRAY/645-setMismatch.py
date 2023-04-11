class Solution:
    def findErrorNums(self, nums):
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]


if __name__ == '__main__':
    nums = [1, 2, 2, 4]
    a = Solution()
    print(a.findErrorNums(nums))
