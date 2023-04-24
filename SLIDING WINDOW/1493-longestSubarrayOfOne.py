class Solution:
    def longestSubarray(self, nums) -> int:
        # just maintain atmost one zero in the window
        k = 1
        left = right = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left


if __name__ == '__main__':
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    a = Solution()
    print(a.longestSubarray(nums))
