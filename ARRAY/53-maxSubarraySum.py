class Solution:
    def maxSubArray(self, nums) -> int:
        # Kadanes Algorithm
        max_sum = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                if sum < 0:
                    sum = nums[i]
                else:
                    sum += nums[i]
                max_sum = max(sum, max_sum)

            elif nums[i] < 0:
                if sum<0:
                    sum=nums[i]
                else:
                    sum += nums[i]
                max_sum = max(sum, max_sum)
        return max_sum


if __name__ == '__main__':
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [-2, -1]
    a = Solution()
    print(a.maxSubArray(nums))
