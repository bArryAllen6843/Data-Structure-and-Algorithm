class Solution:
    def pivotInteger(self, n: int) -> int:
        a = n * (n + 1) // 2
        for x in range(n + 1):
            b, c = x * (x - 1) // 2, x * (x + 1) // 2
            if a - b == c: return x
        return -1


if __name__ == '__main__':
    n = 8
    a = Solution()
    print(a.pivotInteger(n))
