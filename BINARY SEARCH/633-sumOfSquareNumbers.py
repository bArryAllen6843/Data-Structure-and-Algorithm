from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # we can write a as a = sqrt(c - b**2) so that means a < sqrt(c). That's why we make a loop till int(sqrt(c))
        # for that a we can get b**2 = c - a**2 then we got the solution otherwise shift left or right pointer
        for a in range(int(sqrt(c)) + 1):
            target = c - a ** 2
            l, r = 0, sqrt(c)
            while l <= r:
                b = l + (r - l) // 2
                if b * b == target:
                    return True
                elif b * b > target:
                    r = b - 1
                elif b * b < target:
                    l = b + 1
        return False


if __name__ == '__main__':
    c = 5
    a = Solution()
    print(a.judgeSquareSum(c))
