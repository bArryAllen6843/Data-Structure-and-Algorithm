class Solution:
    def isHappy(self, n):
        s = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in s:
                return False
            else:
                s.add(n)
        else:
            return True


if __name__ == '__main__':
    n = 19
    a = Solution()
    print(a.isHappy(n))
