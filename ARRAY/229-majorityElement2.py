class Solution:
    def majorityElement(self, nums):
        if not nums: return []
        num1, num2 = 0, 1
        c1, c2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == num1:
                c1 += 1
            elif nums[i] == num2:
                c2 += 1
            elif c1 == 0:
                num1 = nums[i]
                c1 += 1
            elif c2 == 0:
                num2 = nums[i]
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        return [n for n in (num1, num2)
                if nums.count(n) > len(nums) // 3]


if __name__ == '__main__':
    nums = [3, 2, 3]
    # nums = [2, 2, 1, 3]
    a = Solution()
    print(a.majorityElement(nums))
