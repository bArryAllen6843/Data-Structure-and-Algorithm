class Solution:
    def sortArrayByParityII(self, nums):
        o = 1
        e = 0
        n = len(nums)
        while o < n and e < n - 1:
            if nums[e] % 2 == 0:
                e += 2
            else:
                if nums[o] % 2 == 0:
                    nums[e], nums[o] = nums[o], nums[e]
                else:
                    o += 2
        return nums


if __name__ == '__main__':
    nums = [4, 2, 5, 7]
    a = Solution()
    print(a.sortArrayByParityII(nums))
