class Solution:
    def longestConsecutive(self, nums):
        s, longest = set(nums), 0
        for num in s:
            if num - 1 in s: continue
            j = 1
            while num + j in s: j += 1
            longest = max(longest, j)
        return longest


if __name__ == '__main__':
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    a = Solution()
    print(a.longestConsecutive(nums))
