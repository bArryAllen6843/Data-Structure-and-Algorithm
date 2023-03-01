class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            if s[r] not in seen:
                ans = max(ans, r - l + 1)
            else:
                if seen[s[r]] < l:
                    ans = max(ans, r - l + 1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return ans


if __name__ == '__main__':
    s = "abcabcbb"
    a = Solution()
    print(a.lengthOfLongestSubstring(s))
