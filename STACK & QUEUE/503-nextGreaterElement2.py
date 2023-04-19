class Solution:
    # TC: O(N)
    # SC: O(N)
    def nextGreaterElements(self, nums):
        stack, res = [], [-1] * len(nums)
        # this loop will run in cyclic form
        for i in list(range(len(nums))) * 2:
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 3]
    a = Solution()
    print(a.nextGreaterElements(nums))
