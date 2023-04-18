class Solution:
    # use stack, dictionary to store last occurence and set to store unique value
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        visited = set()
        last_occurence = {}

        for i in range(len(s)):
            last_occurence[s[i]] = i

        for i in range(len(s)):
            if s[i] not in visited:
                while st and st[-1] > s[i] and last_occurence[st[-1]] > i:
                    visited.remove(st.pop())

                st.append(s[i])
                visited.add(s[i])
        return "".join(st)


if __name__ == '__main__':
    a = Solution()
    s = "bcabc"
    print(a.removeDuplicateLetters(s))
