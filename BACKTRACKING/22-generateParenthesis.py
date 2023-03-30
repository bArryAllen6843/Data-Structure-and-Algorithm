class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        curr = []
        opening = closing = n

        def gen(opening, closing):
            if closing < opening or opening == -1 or closing == -1:
                return
            if opening == 0 and closing == 0:
                ans.append("".join(curr))
            else:
                curr.append("(")
                gen(opening - 1, closing)
                curr.pop()

                curr.append(")")
                gen(opening, closing - 1)
                curr.pop()

        gen(opening, closing)
        return ans


if __name__ == '__main__':
    n = 3
    a = Solution()
    print(a.generateParenthesis(n))
