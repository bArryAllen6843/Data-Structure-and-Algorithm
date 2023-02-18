class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i] != '*':
                st.append(s[i])
            elif s[i] == '*':
                st.pop()
                i += 1
        return "".join(st)


if __name__ == '__main__':
    st = 'leet**cod*e'
    a = Solution()
    print(a.removeStars(st))
