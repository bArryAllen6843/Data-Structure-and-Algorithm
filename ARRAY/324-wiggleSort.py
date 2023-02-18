class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
        return nums


if __name__ == '__main__':
    A = [1, 5, 1, 1, 6, 4]
    ss = Solution()
    print(ss.wiggleSort(A))
