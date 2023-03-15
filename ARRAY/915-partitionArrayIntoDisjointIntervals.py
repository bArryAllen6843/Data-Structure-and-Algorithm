class Solution:
    def partitionDisjoint(self, nums) -> int:
        disjoint = 0
        max_left = nums[0]
        max_so_far = nums[0]

        # if out next element is smaller than max_left it means that element should be included in left array
        # so shift the disjoint to that index and disjoint+1 as starting index is 0 not 1
        for i, val in enumerate(nums):
            max_so_far = max(max_so_far, val)
            if max_left > val:
                disjoint = i
                max_left = max_so_far
        return disjoint + 1


if __name__ == '__main__':
    nums = [5, 0, 3, 8, 6]
    a = Solution()
    print(a.partitionDisjoint(nums))
