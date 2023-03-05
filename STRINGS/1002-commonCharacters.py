import collections


class Solution:
    def commonChars(self, A):
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())


if __name__ == '__main__':
    words = ["bella", "label", "roller"]
    a = Solution()
    print(a.commonChars(words))
