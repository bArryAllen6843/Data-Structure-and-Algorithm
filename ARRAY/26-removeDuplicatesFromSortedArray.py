
def removeDuplicates(nums) -> int:
    if nums is None: return 0
    if len(nums) == 1:
        return 1
    prev, curr = 0, 1
    while curr < len(nums):
        if nums[curr] == nums[prev]:
            curr += 1
        else:
            prev += 1
            nums[prev] = nums[curr]
            curr += 1
    return prev + 1


a = [0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(a))
