import collections


class Solution(object):
    def characterReplacement(self, s, k):
        maxlen, largestCount = 0, 0
        arr = collections.Counter()

        for idx in range(len(s)):
            arr[s[idx]] += 1
            largestCount = max(largestCount, arr[s[idx]])

            if maxlen - largestCount >= k:
                arr[s[idx - maxlen]] -= 1
            else:
                maxlen += 1
        return maxlen


if __name__ == '__main__':
    # s = "ABAB"
    # k = 2
    s = "AABABBA"
    k = 1
    a = Solution()
    print(a.characterReplacement(s, k))
