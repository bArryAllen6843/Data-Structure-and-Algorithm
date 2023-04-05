class Solution:
    def minimizeArrayValue(self, nums) -> int:
        sum=0
        res=0
        for i in range(len(nums)):
            sum+=nums[i]
            res=max(res, (sum+1)//(i+1))
        return res

if __name__ == '__main__':
    nums = [3, 7, 1, 6]
    a=Solution()
    print(a.minimizeArrayValue(nums))