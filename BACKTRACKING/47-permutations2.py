class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, paths, res):
        if len(nums) == 0:
            res.append(paths)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i + 1:], paths + [nums[i]], res)


if __name__ == '__main__':
    nums = [1, 2, 3]
    a = Solution()
    print(a.permuteUnique(nums))
