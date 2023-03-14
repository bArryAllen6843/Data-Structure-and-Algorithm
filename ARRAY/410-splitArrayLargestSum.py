class Solution:
    def splitArray(self, nums, k: int) -> int:
        def feasible(threshold):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                    if count > k:
                        return False
            return True
        # same concept as ques 1011
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    k = 2
    a = Solution()
    print(a.splitArray(nums, k))
