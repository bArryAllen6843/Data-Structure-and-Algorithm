from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        res = []
        pcount = Counter(p)
        scount = Counter(s[:len(p) - 1])

        for i in range(len(p) - 1, len(s)):
            scount[s[i]] += 1
            if scount == pcount:
                res.append(i - len(p) + 1)
            scount[s[i - len(p) + 1]] -= 1

            if scount[s[i - len(p) + 1]] == 0:
                del scount[s[i - len(p) + 1]]
        return res


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    a = Solution()
    print(a.findAnagrams(s, p))
