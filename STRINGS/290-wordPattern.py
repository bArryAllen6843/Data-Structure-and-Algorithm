class Solution:

    # POSTED THIS QUESTION ON LEETCODE

    def wordPattern(self, pattern: str, s: str) -> bool:
        map = dict()
        s = s.split(" ")
        if len(pattern)!=len(s):return False
        st=set()
        for i in range(len(s)):
            if s[i] not in map and pattern[i] not in st:
                st.add(pattern[i])
                map[s[i]] = pattern[i]

        # for key, value in map.items():
        #     if value not in st:
        #         st.add(value)
        #     else:
        #         map.popitem()

        for i in range(len(s)):
            if s[i] in map and map[s[i]] == pattern[i]:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat fish"
    # pattern = "aaa"
    # s = "aa aa aa aa"
    a = Solution()
    print(a.wordPattern(pattern, s))
