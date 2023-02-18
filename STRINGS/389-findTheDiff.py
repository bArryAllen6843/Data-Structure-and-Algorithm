# approach1 done through XOR (doubt)
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         c = 0
#         for cs in s: c ^= ord(cs)  # ord is ASCII value
#         for ct in t: c ^= ord(ct)
#         return chr(c)  # chr = convert ASCII into character

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff=0
        for st in t:diff+=ord(st)
        for ss in s:diff-=ord(ss)
        return chr(diff)


if __name__ == '__main__':
    a = 'abcd'
    b = 'abcde'
    ss = Solution()
    print(ss.findTheDifference(a, b))
