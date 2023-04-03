class Solution:
    def specialArray(self, nums) -> int:

        # BRUTE FORCE APPROACH
        # nums.sort()
        # n = len(nums)
        # # edge case (if x is smaller then our first element of nums then all are accepted so return length)
        # if n < nums[0]: return n
        #
        # # Now checking if remaining elements from that index are greater than previous element and greater than or
        # # equal to current element then return those remaining elements
        # for i in range(1, n):
        #     #  prev ele     remaining ele   curr ele
        #     if nums[i - 1]  <  n - i   <=   nums[i]: return n - i
        # return -1

        # BINARY SEARCH
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            x = len(nums) - mid
            if nums[mid] >= x:
                if len(nums) < nums[0]:
                    return len(nums)
                elif mid == 0 or nums[mid - 1] < x:
                    return x
                else:
                    r = mid - 1
            else:
                l = mid + 1
        return -1


if __name__ == '__main__':
    # nums = [0, 4, 3, 0, 4]
    # nums=[3,5]
    # nums=[3,6,7,7,0]
    nums = [3, 9, 7, 8, 3, 8, 6, 6]
    a = Solution()
    print(a.specialArray(nums))
