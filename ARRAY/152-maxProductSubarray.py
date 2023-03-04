class Solution(object):
    def maxProduct(self, nums):
        max_pro, min_pro, ans = nums[0], nums[0], nums[0]

        for i in range(1,len(nums)):
            x = max(nums[i], max_pro * nums[i], min_pro * nums[i])
            y = min(nums[i], max_pro * nums[i], min_pro * nums[i])

            max_pro, min_pro = x, y
            ans = max(max_pro, ans)
        return ans


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    a = Solution()
    print(a.maxProduct(nums))
