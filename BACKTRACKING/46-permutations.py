class Solution:
    def permute(self, nums):
        def recursive(nums, paths, res):
            if not nums: res.append(paths[::])

            for i in range(len(nums)):
                newNums = nums[:i] + nums[i + 1:]
                paths.append(nums[i])
                recursive(newNums, paths, res)
                paths.pop()
            return res

        return recursive(nums, [], [])


if __name__ == '__main__':
    nums = [1, 2, 3]
    a = Solution()
    print(a.permute(nums))
