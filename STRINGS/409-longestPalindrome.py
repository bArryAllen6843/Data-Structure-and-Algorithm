class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        return len(s) - len(hash) + 1 if len(hash) > 1 else len(s)


if __name__ == '__main__':
    s = "abccccdd"
    a = Solution()
    print(a.longestPalindrome(s))
