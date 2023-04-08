# Conditions:
#      1. array length is 1  -> return the only index
#      2. array length is 2  -> return the bigger number's index
#      3. array length is bigger than 2 ->
#            (1) find mid, compare it with its left and right neighbors
#            (2) return mid if nums[mid] greater than both neighbors
#            (3) take the right half array if nums[mid] smaller than right neighbor
#            (4) otherwise, take the left half

class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        # handle condition 3
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        # handle condition 1 and 2
        return left if nums[left] >= nums[right] else right


if __name__ == '__main__':
    # return any one peak's index
    nums = [1, 2, 1, 3, 5, 6, 4]
    a = Solution()
    print(a.findPeakElement(nums))
