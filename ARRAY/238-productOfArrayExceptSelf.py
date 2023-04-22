class Solution:
    def productExceptSelf(self, nums):
        n, ans, suffix_prod = len(nums), [1] * len(nums), 1

        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        for i in range(n - 1, -1, -1):
            ans[i] *= suffix_prod
            suffix_prod *= nums[i]
        return ans

    def productExceptSelf1(self, nums):
        ans, suf, pre = [1] * len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre  # prefix product from one end
            pre *= nums[i]
            ans[-1 - i] *= suf  # suffix product from other end
            suf *= nums[-1 - i]

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    a = Solution()
    print(a.productExceptSelf(nums))
    print(a.productExceptSelf1(nums))
