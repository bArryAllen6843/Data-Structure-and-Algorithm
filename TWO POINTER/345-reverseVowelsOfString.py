class Solution:
    def reverseVowels(self, s: str) -> str:
        # s=list(s)
        s = [*s]
        l, r = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            elif s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)


if __name__ == '__main__':
    s = "hellomandi"
    a = Solution()
    print(a.reverseVowels(s))
