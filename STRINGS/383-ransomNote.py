from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1 = Counter(ransomNote)
        st2 = Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False


if __name__ == '__main__':
    s1 = "fffbfg"
    s2 = "effjfggbffjdgbjjhhdegh"

    a = Solution()
    print(a.canConstruct(s1, s2))
