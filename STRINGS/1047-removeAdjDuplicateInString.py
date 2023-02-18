class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for a in s:
            if len(st) > 0 and st[-1] == a:
                st.pop()
            else:
                st.append(a)
        return "".join(st)


if __name__ == '__main__':
    s = 'abbaca'
    a = Solution()
    print(a.removeDuplicates(s))
