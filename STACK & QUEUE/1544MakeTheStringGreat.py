class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for a in s:
            if st and abs(ord(st[-1]) - ord(a)) == 32:
                st.pop()
            else:
                st.append(a)
        return "".join(st)


if __name__ == '__main__':
    s = 'leEeetcode'
    a = Solution()
    print(a.makeGood(s))
