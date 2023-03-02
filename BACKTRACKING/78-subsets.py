class Solution:
    def subsets(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, paths, res):
        res.append(paths)

        for i in range(len(nums)):
            self.dfs(nums[i + 1:], paths + [nums[i]], res)


if __name__ == '__main__':
    nums = [1, 2, 3]
    a = Solution()
    print(a.subsets(nums))
