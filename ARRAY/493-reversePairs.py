class Solution:
    def reversePairs(self, nums) -> int:
        return mergeSort(nums, 0, len(nums) - 1)


def mergeSort(nums, low, high):
    if low >= high: return 0
    mid = (low + high) // 2
    inv = mergeSort(nums, low, mid)
    inv += mergeSort(nums, mid + 1, high)
    inv += merge(nums, low, mid, high)
    return inv


def merge(nums, low, mid, high):
    count = 0
    j = mid + 1
    for i in range(low, mid + 1):
        while j <= high and nums[i] > 2 * nums[j]:
            j += 1
        count += j - (mid + 1)
    temp = []
    left, right = low, mid + 1
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= high:
        temp.append(nums[right])
        right += 1

    for i in range(low, high + 1):
        nums[i] = temp[i - low]
    return count


if __name__ == '__main__':
    nums = [1, 3, 2, 3, 1]
    a = Solution()
    print(a.reversePairs(nums))
