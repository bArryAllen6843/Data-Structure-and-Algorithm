class Solution:
    def increasingTriplet(self, nums) -> bool:
        # find a triplet with i<j<k and  nums[i] < nums[j] < nums[k]
        first = second = float('inf')
        for el in nums:
            if el <= first:
                first = el
            elif el <= second:
                second = el
            else:
                return True
        return False


if __name__ == '__main__':
    nums = [20, 100, 10, 12, 5, 13]
    a = Solution()
    print(a.increasingTriplet(nums))
