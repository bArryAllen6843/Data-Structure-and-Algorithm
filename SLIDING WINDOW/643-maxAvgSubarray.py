class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        summ=sum(nums[:k])
        max_sum=summ
        for i in range(1,len(nums)-k+1):
            summ-=nums[i-1]
            summ+=nums[i+k-1]
            max_sum=max(max_sum,summ)
        return float(max_sum)/k


if __name__ == '__main__':
    # nums = [1, 12, -5, -6, 50, 3]
    nums=[0, 1, 1, 3, 3]
    k = 4
    # nums=[5]
    # k=1
    a = Solution()
    print(a.findMaxAverage(nums, k))
