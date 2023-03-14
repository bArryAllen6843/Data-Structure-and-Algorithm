import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def enough(mid):
            total = mid // a + mid // b + mid // c - mid // ab - mid // bc - mid // ac + mid // abc
            return total >= n
        # calculate total ugly numbers in range of mid if that total is greater than n then shift right otherwise left
        ab = a * b // math.gcd(a, b)
        bc = c * b // math.gcd(c, b)
        ac = a * c // math.gcd(a, c)
        abc = a * bc // math.gcd(a, bc)
        left, right = 1, 10 ** 10
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    n = 3
    a = 2
    b = 3
    c = 5
    s = Solution()
    print(s.nthUglyNumber(n, a, b, c))
