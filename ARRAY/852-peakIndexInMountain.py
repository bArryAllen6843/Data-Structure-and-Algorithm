class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m
        return l


if __name__ == '__main__':
    arr = [0, 10, 5, 2]
    a = Solution()
    print(a.peakIndexInMountainArray(arr))
