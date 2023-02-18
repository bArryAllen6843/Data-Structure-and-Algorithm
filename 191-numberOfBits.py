class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(n)
        cnt = 0
        for digit in n:
            if digit == "1": cnt += 1
            # elif digit=="0":continue
        return cnt


if __name__ == '__main__':
    n = 000000000000000000000000000001011
    a = Solution()
    print(a.hammingWeight(n))
