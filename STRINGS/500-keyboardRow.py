class Solution:
    def findWords(self, words):
        s1 = list("qwertyuiop")
        s2 = list("asdfghjkl")
        s3 = list("zxcvbnm")
        ans = []
        for word in words:
            flag = 0
            temp = word
            word = word.lower()
            if word[0] in s1:
                res_s = s1
            elif word[0] in s2:
                res_s = s2
            elif word[0] in s3:
                res_s = s3

            for i in range(len(word)):
                if word[i] not in res_s:
                    flag = 1
                    break
            if flag != 1:
                ans.append(temp)

        return ans


if __name__ == '__main__':
    words = ["Hello", "Alaska", "Dad", "Peace"]
    a = Solution()
    print(a.findWords(words))
