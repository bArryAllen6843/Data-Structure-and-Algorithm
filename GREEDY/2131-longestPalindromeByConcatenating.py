import collections


class Solution:
    def longestPalindrome(self, words) -> int:
        counter, ans = [[0] * 26 for _ in range(26)], 0
        for w in words:
            a, b = ord(w[0]) - ord('a'), ord(w[1]) - ord('a')

            if counter[b][a]:
                ans += 4
                counter[b][a] -= 1
            else:
                counter[a][b] += 1

        # if there is a element "gg" then we just increase count by 2 and then break
        for i in range(26):
            if counter[i][i]:
                ans += 2
                break
        return ans


if __name__ == '__main__':
    nums = ["ab", "yt", "cl", "ty", "ab", "lc"]
    a = Solution()
    print(a.longestPalindrome(nums))
