class Solution:

    # BRUTE FORCE
    def canPartition(self, nums):
        def solve(nums, i, sum1, sum2):
            if i >= len(nums): return sum1 == sum2
            return solve(nums, i + 1, sum1 + nums[i], sum2) or solve(nums, i + 1, sum1, sum2 + nums[i])

        return solve(nums, 0, 0, 0)

    # OPTIMIZED
    # Time Complexity : O(2^N) we try both choices of including or excluding an element from subset leading to
    # recursive branches 2*2*2..N times
    # Space Complexity : O(N) recursive stack
    def canPartition1(self, nums):
        def solve1(s, i=0):
            if s==0:return True
            if i>=len(nums) or s<0:return False
            return solve1(s-nums[i],i+1) or solve1(s,i+1)

        total_sum=sum(nums)
        return total_sum & 1 ==0 and solve1(total_sum//2)

    # DP-MEMOIZATION
    # Time Complexity : O(N*sum), where N is the number of elements in nums & sum is the sum of all elements in nums.
    # Space Complexity : O(N*sum), required by dp
    def canPartition2(self, nums):
        total_sum, i = sum(nums), 0

        def subsetSum(s):
            nonlocal i
            if s == 0: return True
            if i >= len(nums) or s < 0: return False
            i += 1
            ans = subsetSum(s - nums[i - 1]) or subsetSum(s)
            i -= 1
            return ans

        return total_sum & 1 == 0 and subsetSum(total_sum // 2)

    # ANOTHER APPROACH
    # Time Complexity : O(N*sum)
    # Space Complexity : O(sum)
    def canPartition3(self,nums):
        total_sum = sum(nums)
        if total_sum & 1: return False
        half_sum, dp = total_sum // 2, 1
        for num in nums:
            dp |= dp << num
        return dp & 1 << half_sum


if __name__ == '__main__':
    nums = [2, 2, 1, 5]
    # nums = [1, 2, 3, 5]
    a = Solution()
    print(a.canPartition(nums))
    print(a.canPartition1(nums))
    print(a.canPartition2(nums))
    print(a.canPartition3(nums))
