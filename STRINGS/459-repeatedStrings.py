
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = (s + s)[1:-1]
        return ss.find(s)!=-1


if __name__ == '__main__':
    s = "abababc"
    a = Solution()
    print(a.repeatedSubstringPattern(s))
