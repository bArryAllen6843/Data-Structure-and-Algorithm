class Solution:
    def searchRange(self, nums, target: int):
        def leftSearch(a, x):
            l, r = 0, len(a) - 1
            while l <= r:
                mid = (l + r) // 2
                if x > a[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def rightSearch(a, x):
            l, r = 0, len(a) - 1
            while l <= r:
                mid = (l + r) // 2
                if x >= a[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        left, right = leftSearch(nums, target), rightSearch(nums, target)
        return [left, right] if left <= right else [-1, -1]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    a = Solution()
    print(a.searchRange(nums, target))
