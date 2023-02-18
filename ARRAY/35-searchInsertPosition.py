def searchInsert(nums, target: int) -> int:
    n = len(nums)
    l = 0
    h = n - 1
    while l <= h:
        mid = (l + h) // 2

        if nums[mid] < target:
            l = mid + 1
            if l >= h:
                if target > nums[h]:
                    return h + 1
                elif target < nums[h]:
                    return h
        elif nums[mid] > target:
            h = mid - 1
            if h <= l:
                if target > nums[l]:
                    return l + 1
                elif target < nums[l]:
                    return l
        else:
            return mid


if __name__ == '__main__':
    a = [1, 3, 5, 6]
    print(searchInsert(a, 2))
