class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(num):
            count = 0
            for row in range(1, m + 1):
                add = min(num // row, n)
                if add == 0: break
                count += add
            return count >= k

        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    m = 3
    n = 3
    k = 5
    a = Solution()
    print(a.findKthNumber(m, n, k))
