class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if abs(target - s) < abs(target - res):
                    res = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return res
        return res


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    a = Solution()
    print(a.threeSumClosest(nums, target))
