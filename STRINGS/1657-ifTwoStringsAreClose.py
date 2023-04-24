from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
        cnt1=Counter(word1).values()
        cnt2=Counter(word2).values()
        c=Counter(cnt1)
        cc=Counter(cnt2)
        return set(word1) == set(word2) and c==cc

if __name__ == '__main__':
    word1 = "cabbba"
    word2 = "abbcccab"
    a = Solution()
    print(a.closeStrings(word1, word2))
#     You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
