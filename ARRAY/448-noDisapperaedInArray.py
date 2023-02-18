# Time Complexity : O(n), we only iterate nums twice each taking O(n) time atmost.
# Space Complexity : O(1), only constant extra space is being used except for the output ans
def find(nums):
    ans = []
    for c in nums:
        nums[abs(c) - 1] = -abs(nums[abs(c) - 1])
    # print(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            ans.append(i+1)
    return ans


if __name__ == '__main__':
    a = [4, 3, 2, 7, 8, 2, 3, 1]
    print(find(a))
