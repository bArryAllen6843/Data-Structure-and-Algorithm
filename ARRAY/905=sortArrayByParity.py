class Solution:
    def sortArrayByParity(self, nums):
        l = 0
        n = len(nums)
        r = n - 1
        while l <= r:
            if nums[l] % 2 != 0:
                temp = nums[l]
                arr=nums
                for i in range(l, n - 1):
                    arr[i] = arr[i + 1]
                arr[-1] = temp
            elif nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 != 0:
                r -= 1
        return nums


if __name__ == '__main__':
    # nums = [3, 1, 2, 4]
    nums=[2,6,8,3,1,2,4]
    a = Solution()
    print(a.sortArrayByParity(nums))
