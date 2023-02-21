class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        l = 0
        h = n - 1
        while l < h:
            mid = l + (h - l) // 2
            # The pairs which are on the left of the single element, will have the first element in an even position
            # and the    second element at an odd position. All the pairs which are on the right side of the single
            # element will have the first position at an odd position and the second element at an even position
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                l = mid + 1
            else:
                h = mid
        return nums[l]


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    a = Solution()
    print(a.singleNonDuplicate(nums))
