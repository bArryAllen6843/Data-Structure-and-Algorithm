class Solution:
    def search(self, nums, target: int) -> int:
        if not nums: return -1
        l = 0
        n = len(nums)
        h = n - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    a = Solution()
    print(a.search(nums, target))
