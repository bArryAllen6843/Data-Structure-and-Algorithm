class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        def f(divisor):
            return sum(((num - 1) // divisor )+ 1 for num in nums) <= threshold

        # smaller the divisor bigger is the threshold
        # so if a divisor is giving smaller or equal value then threshold it means we have to increase threshold by
        # decreasing divisor and to decrease divisor we need to shift right pointer to mid same goes for left pointer
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    nums = [1, 2, 5, 9]
    threshold = 6
    a = Solution()
    print(a.smallestDivisor(nums, threshold))
