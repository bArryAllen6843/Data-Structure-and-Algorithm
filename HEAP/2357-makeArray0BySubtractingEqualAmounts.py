class Solution:
    def minimumOperations(self, nums):
        return len(set(nums) - {0})


if __name__ == '__main__':
    a = Solution()
    nums = [1, 5, 0, 3, 5, 4, 6]
    print(a.minimumOperations(nums))
