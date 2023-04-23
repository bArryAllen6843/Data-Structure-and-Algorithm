class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = ans = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i, c in enumerate(s):
            if c in vowels:
                cnt += 1
            if i >= k and s[i - k] in vowels:
                cnt -= 1
            ans = max(ans, cnt)
        return ans


if __name__ == '__main__':
    s = "leetcode"
    k = 3
    # s = "abciiidef"
    # k = 3
    a = Solution()
    print(a.maxVowels(s, k))
