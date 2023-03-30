from itertools import accumulate


class Solution:
    def find132pattern(self, nums) -> bool:
        min_list = list(accumulate(nums, min))
        stack, n = [], len(nums)

        for j in range(n - 1, -1, -1):
            if nums[j] > min_list[j]:
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False


if __name__ == '__main__':
    nums = [3, 1, 4, 2]
    a = Solution()
    print(a.find132pattern(nums))
